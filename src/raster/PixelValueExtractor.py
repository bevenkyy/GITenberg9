# -*-coding:utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from osgeo import gdal, osr, gdalconst

def query_geotiff_info(in_file_path):
    '''
    根据指定的图像文件路径，以只读的方式打开图像。（仅支持Tif格式）

    :param in_file_path: 输入的文件路径，目前仅支持tif（TIF）格式的文件
    :return: gdal数据集、地理空间坐标系、投影坐标系、栅格影像的大小相关信息
    '''
    #
    geotiff_info = {}
    #
    if in_file_path.endswith(".tif") or in_file_path.endswith(".TIF"):
        dataset = gdal.Open(in_file_path)
        #
        geotiff_info["band_count"] = dataset.RasterCount
        geotiff_info["geotransform"] = dataset.GetGeoTransform()
        geotiff_info["band_width"] = dataset.RasterXSize
        geotiff_info["band_height"] = dataset.RasterYSize
        #
        pcs = osr.SpatialReference()
        pcs.ImportFromWkt(dataset.GetProjection())
        gcs = pcs.CloneGeogCS()
        geotiff_info["gcs"] = gcs
        geotiff_info["pcs"] = pcs

    else:
        raise("Unsupported file format!")
    #
    dataset = None
    #
    return geotiff_info

def lonlat_to_xy(gcs, pcs, lon, lat):
    '''
    经纬度坐标转换为投影坐标

    :param gcs: 地理空间坐标信息，可由get_file_info（）函数获取
    :param pcs: 投影坐标信息，可由get_file_info（）函数获取
    :param lon: 经度坐标
    :param lat: 纬度坐标
    :return: 地理空间坐标对应的投影坐标
    '''
    #
    ct = osr.CoordinateTransformation(gcs, pcs)
    coordinates = ct.TransformPoint(lon, lat)
    x, y, _ = coordinates
    #
    return x, y

def xy_to_lonlat(gcs, pcs, x, y):
    '''
    投影坐标转换为经纬度坐标

    :param gcs: 地理空间坐标信息，可由get_file_info（）函数获取
    :param pcs: 投影坐标信息，可由get_file_info（）函数获取
    :param x: 像元的行号
    :param y: 像元的列号
    :return: 投影坐标对应的地理空间坐标
    '''
    #
    ct = osr.CoordinateTransformation(pcs, gcs)
    lon, lat, _ = ct.TransformPoint(x, y)
    #
    return lon, lat

def xy_to_rowcol(extend, x, y):
    '''
    根据GDAL的六参数模型将给定的投影坐标转为影像图上坐标（行列号）

    根据GDAL的六 参数模型将给定的投影或地理坐标转为影像图上坐标（行列号）
    :param extend: 图像的空间范围
    :param x: 投影坐标x
    :param y: 投影坐标y
    :return: 投影坐标(x, y)对应的影像图上行列号(row, col)
    '''
    a = np.array([[extend[1], extend[2]], [extend[4], extend[5]]])
    b = np.array([x - extend[0], y - extend[3]])
    #
    try:
        row_col = np.linalg.solve(a, b)  # 使用numpy的linalg.solve进行二元一次方程的求解
        row = np.int(np.floor(row_col[0])) #行，Y（竖直）方向
        col = np.int(np.floor(row_col[1])) #列，X（水平）方向
    except ValueError:
        return -1, -1
    #
    return col, row

def rowcol_to_xy(extend, col, row):
    '''
    图像坐标转换为投影坐标

    根据GDAL的六参数模型将影像图上坐标（行列号）转为投影坐标或地理坐标（根据具体数据的坐标系统转换）
    :param extend: 图像的空间范围
    :param col: 像元的列号,X（水平）方向的坐标
    :param row: 像元的行号,Y（竖直）方向的坐标
    :return: 行列号(row, col)对应的投影坐标(x, y)
    '''
    #
    x = extend[0] + row * extend[1] + col * extend[2]
    y = extend[3] + row * extend[4] + col * extend[5]
    #
    return x, y

def lonlat_to_rowcol(gcs, pcs, extend, lon, lat):
    '''
    图像坐标转换为投影坐标

    根据GDAL的六参数模型将影像图上坐标（行列号）转为投影坐标或地理坐标（根据具体数据的坐标系统转换）
    :param extend: 图像的空间范围
    :param row: 像元的行号
    :param col: 像元的列号
    :return: 行列号(row, col)对应的投影坐标(x, y)
    '''
    #
    x, y = lonlat_to_xy(gcs, pcs, lon ,lat)
    col, row = xy_to_rowcol(extend, x, y)
    #
    return col, row

def rowcol_to_lonlat(gcs, pcs, extend, col, row):
    '''
    图像坐标转换为投影坐标

    根据GDAL的六参数模型将影像图上坐标（行列号）转为投影坐标或地理坐标（根据具体数据的坐标系统转换）
    :param extend: 图像的空间范围
    :param row: 像元的行号
    :param col: 像元的列号
    :return: 行列号(row, col)对应的投影坐标(x, y)
    '''
    #
    x, y = rowcol_to_xy(extend, col, row)
    lon, lat = xy_to_lonlat(gcs, pcs, x, y)
    #
    return lon, lat

def get_value_by_coordinates(img_arr, band_count, gcs, pcs, geotransform,
                             coordinates, coordinates_type = "rowcol", 
                             noData = 65536, invalidPixel = 65536):
    '''
    直接根据图像坐标，或者依据GDAL的六参数模型将给定的投影、地理坐标转为影像图上坐标后，返回对应像元的像元值

    :param img_arr: 图像数组，numpy.ndarray类型
    :param coordinates: 坐标，2个元素的元组（X方向，Y方向），比如（经度、纬度）、（列号、行号），坐标为如下三种中的一种像元的行列号、投影坐标或者地理空间坐标
    :param coordinates_type: 坐标类型，“rowcol”、“xy”、“lonlat”
    :return: 指定坐标的像元值
    '''
    #
    value = np.nan
    row = col = 0
    #
    if coordinates_type == "rowcol":
        value = img_arr[coordinates[0],coordinates[1]]
    elif coordinates_type == "lonlat":
        x, y = lonlat_to_xy(gcs, pcs, coordinates[0], coordinates[1])
        col, row = xy_to_rowcol(geotransform, x, y)
        if col == -1 or row == -1:
            pass
        else:
            value = img_arr[row, col]
    elif coordinates_type == "xy":
        col, row = xy_to_rowcol(geotransform, coordinates[0], coordinates[1])
        if col == -1 or row == -1:
            pass
        else:
            value = img_arr[row, col]
    else:
        raise Exception('''"coordinates_type":Wrong parameters input''')
    #
    return value

if __name__ == "__main__":
    #   
    file_path = r"D:\xingrui94\Studying\Project_01\Result\CDOM\band145_Ratio\Sentinel2_Rrs_201808_Mosaic_60m_band145Ratio_fit_clip.tif"
    #
    geotiff_info = query_geotiff_info(file_path)
    #
    col, row = lonlat_to_rowcol(geotiff_info.get("gcs"), geotiff_info.get("pcs"), geotiff_info.get("geotransform"), 121.891100338, 41.0500928418)
    lon, lat = rowcol_to_lonlat(geotiff_info.get("gcs"), geotiff_info.get("pcs"), geotiff_info.get("geotransform"), col, row)
    print(col, row)
    print(lon, lat)

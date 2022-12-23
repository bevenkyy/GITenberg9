# -*- coding:utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import re
from osgeo import gdal, osr, gdalconst
import numpy as np


def query_geotiff_data(file_path):
    '''
    '''
    geotiff_info = {}
    #
    dataset = gdal.Open(file_path, gdalconst.GA_ReadOnly)
    #
    geotiff_info["band_count"] = dataset.RasterCount
    geotiff_info["band_width"] = dataset.RasterXSize
    geotiff_info["band_height"] = dataset.RasterYSize
    geotiff_info["projection"] = dataset.GetProjection()
    geotiff_info["geo_transform"] = dataset.GetGeoTransform()
    #
    dataset = None
    #
    return geotiff_info


def read_geotiff(file_path, index = None, xoff = 0, yoff = 0,
                 win_xsize = None, win_ysize = None, buf_type = None):
    '''
    '''
    img_dcit = {}
    #
    dataset = gdal.Open(file_path, gdalconst.GA_ReadOnly)
    #
    if index == None:
        for i in range(dataset.RasterCount):
            band = dataset.GetRasterBand(i + 1)
            img_dcit["B" + str(i)] = band.ReadAsArray(xoff, yoff, win_xsize, win_ysize, buf_type)
    elif type(index) == int:
        if index > dataset.RasterCount:
            raise Exception("Invalid image index parameter!")
        else:
            band = dataset.GetRasterBand(i + 1)
            img_dcit["B" + str(i)] = band.ReadAsArray(xoff, yoff, win_xsize, win_ysize, buf_type)
    elif type(index) == tuple or type(index) == list:
        for i in index:
            if i > dataset.RasterCount:
                    raise Exception("Invalid image index parameter!")
            else:
                band = dataset.GetRasterBand(i + 1)
                img_dcit["B" + str(i)] = band.ReadAsArray(xoff, yoff, win_xsize, win_ysize, buf_type)
    else:
        raise Exception("Index parameter must be the type: int, tuple or list!")
    #
    dataset = None
    #
    return img_dcit


def write_geotiff(file_path, img, index = None, geotransform = None, projection = None):
    '''
    '''
    img_shape = img.get("B1").shape
    for _, img in img.items():
        if img_shape != img.shape:
            raise Exception("Image dimension must be same!")
        else:
            img_shape = img.shape
    #
    band_height, band_width  = img.shape
    driver = gdal.GetDriverByName("GTiff")
    #
    if len(img) == 1 and type(index) == int:
        dataset = driver.Create(file_path, band_width, band_height, 1, GDT_Float64)
        if dataset != None:
            dataset.SetGeoTransform(geotransform)
            dataset.SetProjection(projection)
            #
            band = dataset.GetRasterBand(1)
            band.WriteArray(img)
        else:
            raise Exception("Failed to write tiff!")
    elif type(index) == tuple or type(index) == list:
        dataset = driver.Create(file_path, band_width, band_height, len(index), GDT_Float64)
        if dataset != None:
            dataset.SetGeoTransform(geotransform)
            dataset.SetProjection(projection)
            #
            for i in index:
                if type(i) != int:
                    raise Exception("Index must be int type!")
                else:
                    for band_name, img in img.items():
                        if int(re.findall("\d+", band_name)[0]) == i:
                            band = dataset.GetRasterBand(i)
                            band.WriteArray(img)
                            #
                            break
        else:
            raise Exception("Failed to write tiff!")
    else:
        raise Exception("Index parameter must be the type: int, tuple or list!")


def query_multidimension_data(file_path):
    '''
    '''
    dataset = gdal.Open(file_name, GA_ReadOnly)
    subdataset_list = dataset.GetSubDatasets()
    #
    dataset = None
    #
    return subdataset_list


def read_hdf(file_path, variable_name = None, index = None, xoff = 0, yoff = 0,
             win_xsize = None, win_ysize = None, buf_type = None):
    '''
    '''
    img_dict = {}
    #
    hdf_file_path = file_path + variable_name
    read_geotiff(variable_name, index, xoff, yoff, win_xsize, win_ysize, buf_type)
    

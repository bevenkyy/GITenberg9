# -*- coding:utf-8 -*-

import os
import sys
from collections import OrderedDict

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import rasterio
import numpy as np


def query_geotiff_info(file_path):
    '''
    '''
    img_info = OrderedDict()
    with rasterio.open(file_path,"r") as dataset:
        img_info["band_count"] = dataset.count
        img_info["band_width"] = dataset.width
        img_info["band_height"] = dataset.height
        img_info["crs"] = dataset.crs
        img_info["transform"] = dataset.transform
    #
    return img_info


def query_valid_band(file_path):
    geotiff_info = query_geotiff_info(file_path)
    valid_band = "B1"
    if geotiff_info.get("band_count") < 2:
        pass
    else:
        for i in range(geotiff_info.get("band_count") - 1):
            valid_band += ",B" + str(i + 2)
    #
    return valid_band

def read_geotiff(file_path, index = None, noData=None):
    '''
    '''
    img_dcit = OrderedDict()
    with rasterio.open(file_path,"r") as dataset:
        #
        if index == None:
            for i in range(dataset.count):
                img = dataset.read(i + 1)
##                # 改变原始数据的形状
##                #     0       1       2          1       2       0      
##                # (通道数，图片高，图片宽) -> (图片高，图片宽，通道数)
##                img = np.transpose(tmp_img, (1, 2, 0)).astype(np.float32)
                img_dcit["B" + str(i)] = img.astype(np.float64)
        else:
            if index > dataset.count:
                raise Exception("Invalid image index!")
            else:
                img = dataset.read(index)
##                img = np.transpose(tmp_img, (1, 2, 0)).astype(np.float32)
                img_dcit["B"  + str(index)] = img.astype(np.float64)
    #
    return img_dcit

def read_single_band(file_path, index):
    with rasterio.open(file_path,"r") as dataset:
        #
        img = dataset.read(index)
    #
    return img


def read_multi_band(file_path, index_list):
    with rasterio.open(file_path,"r") as dataset:
        #
        img = dataset.read(index_list)
    #
    return img

def read_single_scale_band(file_path, index, scale_width, scale_height):
    with rasterio.open(file_path,"r") as dataset:
        #
        img = dataset.read(index, out_shape = (scale_height, scale_width))
    #
    return img

def read_multi_scale_band(file_path, index_list, scale_width, scale_height):
    with rasterio.open(file_path,"r") as dataset:
        #
        img = dataset.read(index_list, out_shape = (scale_height, scale_width))
    #
    return img

def write_single_band(file_path, img_arr, crs, transform):
    with rasterio.open(file_path, 'w',
                       driver = 'GTiff',
                       height = img_arr.shape[0],
                       width = img_arr.shape[1],
                       count = 1,
                       dtype = img_arr.dtype,
                       crs = crs,
                       transform = transform) as dataset:
        dataset.write(img_arr, 1)

        
def write_multi_band(file_path, img_arr, index_list, crs, transform):
    with rasterio.open(file_path, 'w',
                       driver = 'GTiff',
                       height = img_arr.shape[1],
                       width = img_arr.shape[2],
                       count = len(index_list),
                       dtype = img_arr.dtype,
                       crs = crs,
                       transform = transform) as dataset:
        dataset.write(img_arr, list(range(1,len(index_list) + 1)))

def write_geotiff(file_path, img_dict, crs, transform):
    '''
    '''
    band_count = len(img_dict)
    img_list = []
    #
    for _, band in img_dict.items():
        img_list.append(band)
    img_array = np.array(img_list)
    band_height = img_array.shape[1]
    band_width = img_array.shape[2]
    dtype = img_array.dtype
    #
    with rasterio.open(file_path, 'w',
                       driver = 'GTiff',
                       height = band_height,
                       width = band_width,
                       count = band_count,
                       dtype = dtype,
                       crs = crs,
                       transform = transform) as dataset:
        dataset.write(img_array)

def convert_vector_to_2darray(vector, img_width, img_heigh):
    '''
    '''
    return np.reshape(vector,[img_heigh, img_width])


def convert_img_to_2darray(file_path):
    '''
    '''
    img_dcit = read_geotiff(file_path)
    img_info = query_geotiff_info(file_path)
    #
    img_width = img_info.get("band_width")
    img_height = img_info.get("band_height")
    img_band_count = img_info.get("band_count")
    #
    samples_data = np.zeros([img_width * img_height, img_band_count], dtype=np.float64)
    for i, (_, img_arr) in enumerate(img_dcit.items()):
        samples_data[:,i] = img_arr.reshape((img_width * img_height))
    #
    return samples_data


if __name__ == "__main__":
    pass

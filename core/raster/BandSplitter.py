# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import re
import numpy as np

from fileIO import RasterImgIO


def extract_sub_multi_band(in_file_name, band_index_list, save_format, save_file_name):
    '''
    '''
    geotiff_info = RasterImgIO.query_geotiff_info(in_file_name)
    img = RasterImgIO.read_multi_band(in_file_name, band_index_list)
    if save_format == ".tif":
        RasterImgIO.write_multi_band(save_file_name, img, band_index_list, geotiff_info.get("crs") , geotiff_info.get("transform"))
    elif save_format == ".jpg":
        pass
        #RasterImgIO.write_jpeg(save_file_name, img, band_index_list)      


def extract_single_band(in_file_name, band_index_list, save_format, save_file_name):
    geotiff_info = RasterImgIO.query_geotiff_info(in_file_name)
    for index in band_index_list:
        img = RasterImgIO.read_single_band(in_file_name, index)
        tmp_save_file_name = os.path.splitext(save_file_name)[0] + str(index) + os.path.splitext(save_file_name)[1]
        #
        if save_format == ".tif":
            RasterImgIO.write_single_band(tmp_save_file_name, img, geotiff_info.get("crs") , geotiff_info.get("transform"))
        elif save_format == ".jpg":
            pass
            #RasterImgIO.write_jpeg(save_file_name, img, band_index_list)

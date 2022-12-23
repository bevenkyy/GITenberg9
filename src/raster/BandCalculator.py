# -*- coding: utf-8 -*-

import os
import sys
from collections import OrderedDict

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import re
import numpy as np
import numexpr as ne

from fileio import RasterImgIO


def parse_formula(formula_str):
    '''
    '''
    band_index = []
    re_str = r"B\d"
    band_str_list = re.findall(re_str, formula_str)
    for band_str in set(band_str_list):
        for index_char in band_str:
            if index_char.isdigit():
                band_index.append(int(index_char))
    #
    return band_index

def band_calc_(img_dict, formula_str):
    '''
    '''
    out_img_dict = OrderedDict()
    if type(formula_str) == str:
        out_img_dict[formula_str] = ne.evaluate(formula_str,
                                                local_dict = img_dict)
    elif type(formula_str) == tuple or type(formula_str) == list:
        for sub_formula_str in formula_str:
            #
            out_img_dict[sub_formula_str] = ne.evaluate(sub_formula_str,
                                                        local_dict = img_dict)
    else:
        raise Exception('''Invalid parameter "formula", which must be a str, tuple or list''')
    #
    return out_img_dict

def band_calc(formula_str, file_list):
    '''
    '''
    src_img = OrderedDict()
    #
    for i in range(len(file_list)):
        #
        geo_info = RasterImgIO.query_geotiff_info(file_list[i][0])
        src_img.update(RasterImgIO.read_geotiff(file_list[i][0]))
        #
        calc_img = band_calc_(src_img, formula_str)
        out_img = OrderedDict(src_img, **calc_img)
        RasterImgIO.write_geotiff(file_list[i][1], out_img, geo_info.get("crs"), geo_info.get("transform"))

# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np


def dict_to_2darray(data, last_key):
    '''
    '''
    col_title = []
    tmp_data = []
    for key, value in data.items():
        if last_key == None:
            col_title.append(key)
            tmp_data.append(value)
        else:
            if key != last_key:
                col_title.append(key)
                tmp_data.append(value)
    #
    if last_key != None:
        col_title.append(last_key)
        tmp_data.append(data.get(last_key))
    #
    out_data = np.array(tmp_data)
    sampels = out_data.transpose()
    #
    return sampels, col_title
    

if __name__ == "__main__":
    pass

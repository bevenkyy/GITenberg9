# -*- coding: utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def sklearn_process_invalid_value(src_data):
    '''
    '''
    imputer = SimpleImputer(strategy='mean')    
    dst_data = imputer.fit_transform(src_data)
    #
    return dst_data

def np_process_invalid_value(data):
    '''
    '''
    masked_array = np.ma.masked_invalid(data)
    data[masked_array.mask] = -100
    #
    return data

def min_max_scaler(X, scale_range = (0, 1)):
    '''
    '''
    scaler = MinMaxScaler(scale_range)
    scaler_X = scaler.fit_transform(X)
    #
    return scaler_X

def standard_scaler(X):
    '''
    '''
    scaler = StandardScaler()
    scaler_X = scaler.fit_transform(X)
    #
    return scaler_X
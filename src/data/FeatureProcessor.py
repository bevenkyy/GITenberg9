# -*- coding: utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import re
import numpy as np
import numexpr as ne
from scipy.spatial.distance import pdist, squareform
from utils import convert_data_structure


def get_initialization_feature(features_count):
    '''
    '''
    initialization_features_str = "F1"
    for i in range(1, features_count):
        initialization_features_str += ";F" + str(i + 1)
    #
    return initialization_features_str


def parse_sample_feature(samples, features_str):
    '''
    '''
    features_name_list = features_str.split(";")
    features_info_dict = {}
    #
    re_str = r"F\d*"
    #
    for i, features_name in enumerate(features_name_list):
        #
        features_info_dict[features_name] = samples[:, i]
    features_info_dict["y_true"] = samples[:,-1]
    #
    return features_info_dict

def make_feature(samples, features_str):
    features_name_list = features_str.split(";")
    features_info_dict = {}
    #
    re_str = r"F\d*"
    #
    for features_name in features_name_list:
        feature_index = ""
        #
        if len(features_name) <= 4:
            for char in features_name:
                if char.isdigit():
                    feature_index += char
            #
            features_info_dict[features_name] = samples[:, int(feature_index) - 1]
        else:
            tmp_dict = {}
            sub_feature_name_list = re.findall(re_str, features_name)
            for sub_feature_name in set(sub_feature_name_list):
                feature_index = ""
                for char in sub_feature_name:
                    if char.isdigit():
                        feature_index += char
                #
                tmp_dict[sub_feature_name] = samples[:, int(feature_index) - 1]
            #
            combinationSample = eval(features_name, tmp_dict)
            features_info_dict[features_name] = combinationSample
    #
    features_info_dict["y_true"] = samples[:,-1]
    #
    return features_info_dict


def unify_feature(samples, features_str):
    features_name_list = features_str.split(",")
    features_info_dict = {}
    #
    re_str = r"F\d*"
    #
    for features_name in features_name_list:
        feature_index = ""
        #
        if len(features_name) <= 4:
            for char in features_name:
                if char.isdigit():
                    feature_index += char
            #
            features_info_dict[features_name] = samples[:, int(feature_index) - 1]
        else:
            tmp_dict = {}
            sub_feature_name_list = re.findall(re_str, features_name)
            for sub_feature_name in set(sub_feature_name_list):
                feature_index = ""
                for char in sub_feature_name:
                    if char.isdigit():
                        feature_index += char
                #
                tmp_dict[sub_feature_name] = samples[:, int(feature_index) - 1]
            #
            combinationSample = eval(features_name, tmp_dict)
            features_info_dict[features_name] = combinationSample
    #
    return features_info_dict


def calculate_variance(x):
    '''
    '''
    variance = np.var(x)
    #
    return variance

def calculate_pearson_correlation(x1, x2):
    '''
    '''
    # features_correlation = np.zeros([len(valid_samples) - 1, len(valid_samples) - 1], dtype=np.float64)
    # feature_name_list = [key for key, _ in valid_samples.items() if key != "y_true"]
    # for i, feature_name_i in enumerate(feature_name_list):
    #     for j, feature_name_j in enumerate(feature_name_list):
    #         feature_i = valid_samples.get(feature_name_i)
    #         feature_j = valid_samples.get(feature_name_j)
    correlation = np.corrcoef(x1, x2)[0,1]
    #
    return correlation

def calculate_distance_correlation(x, y):
    """ Compute the distance correlation function
    x:a vector
    y:a vector
    return:distance correlation coefficient
    """
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    if np.prod(x.shape) == len(x):
        x = x[:, None]
    if np.prod(y.shape) == len(y):
        y = y[:, None]
    x = np.atleast_2d(x)
    y = np.atleast_2d(y)
    n = x.shape[0]
    if x.shape[0] != y.shape[0]:
        raise ValueError('Number of samples must match')
    a = squareform(pdist(x))
    b = squareform(pdist(y))
    A = a - a.mean(axis=0)[None, :] - a.mean(axis=1)[:, None] + a.mean()
    B = b - b.mean(axis=0)[None, :] - b.mean(axis=1)[:, None] + b.mean()
    
    d_cov2_xy = (A * B).sum()/float(n * n)
    d_cov2_xx = (A * A).sum()/float(n * n)
    d_cov2_yy = (B * B).sum()/float(n * n)
    d_corr = np.sqrt(d_cov2_xy)/np.sqrt(np.sqrt(d_cov2_xx) * np.sqrt(d_cov2_yy))
    #
    return d_corr

def parse_one_feature_ratio(feature_str):
    #
    one_feature_ratio = []
    re_str = "F\d*"
    feature_list = re.findall(re_str, feature_str)
    #
    for feature_name_i in feature_list:
        for feature_name_j in feature_list:
            if feature_name_i != feature_name_j:
                one_feature_ratio.append(feature_name_i + " / " + feature_name_j)
    #
    return one_feature_ratio

def parse_two_feature_sum_difference_ratio(feature_str):
    #
    two_feature_sum = []
    two_feature_difference = []
    two_feature_sum_difference_ratio = []
    re_str = "F\d*"
    feature_list = re.findall(re_str, feature_str)
    #
    feature_list_length = len(feature_list)
    #
    for i in range(feature_list_length):
        if i == feature_list_length - 1:
            break
        for j in range(i + 1, feature_list_length):
            two_feature_sum.append("(" + feature_list[i] + " + " + feature_list[j] + ")")
    #
    for i in range(feature_list_length):
        for j in range(feature_list_length):
            if feature_list[i] != feature_list[j]:
                two_feature_difference.append("(" + feature_list[i] + " - " + feature_list[j] + ")")
    #
    for feature_sum in two_feature_sum:
        for feature_difference in two_feature_difference:
            two_feature_sum_difference_ratio.append(feature_sum + " / " + feature_difference)
    #
    for feature_difference in two_feature_difference:
        for feature_sum in two_feature_sum:
            two_feature_sum_difference_ratio.append(feature_difference + " / " + feature_sum)
    #
    return two_feature_sum_difference_ratio

def feature_calculator(sample, feature_str, feature_calculation_list):
    #
    new_sample_dict = {}
    features_info_dict = parse_sample_feature(sample.astype(np.float32), feature_str)
    #
    for feature_calculation in feature_calculation_list:
        # new_sample_dict[feature_calculation] = eval(feature_calculation, features_info_dict)
        new_sample_dict[feature_calculation] = ne.evaluate(feature_calculation, local_dict = features_info_dict)
    new_sample, col_title = convert_data_structure.dict_to_2darray(new_sample_dict, None)
    #
    return new_sample, col_title

if __name__ == "__main__":
    #
    x = np.arange(-10,11)
    y = x ** 2
    print(x,'\n',y)
    #
    p_corr = round(calculate_pearson_correlation(x,y),6)
    print(p_corr)
    d_corr = round(calculate_distance_correlation(x, y),6)
    print(d_corr)

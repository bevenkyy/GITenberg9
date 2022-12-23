# -*- coding: utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import random
import numpy as np
from sklearn.model_selection import train_test_split
from fileio import ExcelIO



def sort_sampels(data_array):
    '''
    '''
    return data_array[data_array[:,-1].argsort()]


def _sampling_index(start_index:int, stop_index:int, group_samples_count:int)->np.ndarray:
    '''
    返回在start_index, stop_index之间的group_samples_count个均匀间隔的索引
    '''
    tmp_sampling_index = np.linspace(start_index, stop_index, group_samples_count)
    sampling_index = np.floor(tmp_sampling_index).astype(int)
    #
    return sampling_index

def stratified_sampling(data_array, trainval_samples_count, test_samples_count, group_samples_count, 
                        true_train_samples_count, true_test_samples_count):
    '''
    模拟分层抽样
    '''
    trainval_samples = np.zeros([trainval_samples_count, data_array.shape[1]], dtype = np.float64)
    test_samples = np.zeros([test_samples_count, data_array.shape[1]], dtype = np.float64)
    #
    k = 0
    t = 0
    stop_index = -1
    step = int(np.floor(data_array.shape[0] / 10.0))
    #
    for i in range(0, data_array.shape[0], step):
        if i + step <= data_array.shape[0]:
            sampling_index_tuple = _sampling_index(i, i + step - 1, group_samples_count)
            for j in range(i, i + step, 1):
                if j in sampling_index_tuple and k < test_samples_count:
                    test_samples[k] = data_array[j, :]
                    k+=1
                if j not in sampling_index_tuple and t < trainval_samples_count:
                    trainval_samples[t] = data_array[j, :]
                    t+=1
        else:
            stop_index = i
            break
    #
    remaining_samples_count = data_array.shape[0] - (test_samples_count + trainval_samples_count) 
    remaining_samples = np.zeros([remaining_samples_count, data_array.shape[1]], dtype = np.float64)
    n = 0
    for each_sample in data_array.tolist():
        if each_sample not in trainval_samples.tolist() and each_sample not in test_samples.tolist():
            remaining_samples[n, :] = np.array(each_sample)[np.newaxis,:]
            n += 1
    #
    test_remaining_samples_count = abs(test_samples.shape[0] - true_test_samples_count)
    test_remaining_samples_index = _sampling_index(0, remaining_samples.shape[0] - 1, test_remaining_samples_count)
    for m in range(remaining_samples.shape[0]):
        if m in test_remaining_samples_index:
            test_samples = np.append(test_samples, remaining_samples[m, :][np.newaxis,:], axis = 0)
        else:
            trainval_samples = np.append(trainval_samples, remaining_samples[m, :][np.newaxis,:], axis = 0)                       

    return trainval_samples, test_samples


def trainval_test_split(data_array, split_size):
    '''
    '''
    # 用户选择划分比列后的真是样本数
    true_trainval_samples_count = int(np.floor(data_array.shape[0] * (1 - split_size)))
    true_test_samples_count = int(np.floor(data_array.shape[0] * split_size))
    
    # 整数个批次分层后，样本数，须做处理以达到真实样本数
    trainval_samples_count = int(np.floor(true_trainval_samples_count / 10.0)) * 10
    test_samples_count = int(np.floor(true_test_samples_count / 10.0)) * 10
    group_samples_count = int(np.floor(test_samples_count / 10.0))
    #
    trainval_samples, test_samples = stratified_sampling(sort_sampels(data_array),
                                                         trainval_samples_count, 
                                                         test_samples_count,
                                                         group_samples_count,
                                                         true_trainval_samples_count,
                                                         true_test_samples_count)
    np.random.shuffle(trainval_samples)
    np.random.shuffle(test_samples)
    #
    return trainval_samples, test_samples


def sklearn_trainval_test_split(data_array, test_size):
    '''
    '''
    X = data_array[:, :-1]
    y = data_array[:, -1]
    X_trainval, X_test, y_trainval, y_test = train_test_split(X, y, test_size = test_size)
    #
    trainval_samples = np.hstack((X_trainval, y_trainval[:, np.newaxis]))
    test_samples = np.hstack((X_test, y_test[:, np.newaxis]))
    #
    return trainval_samples, test_samples
    


if __name__ == "__main__":
    #
    excel_data = ExcelIO.read_excel(r"C:\Users\lenovo\Desktop\CDOM_Landsat8_Samples.xlsx", True, True)
    trainval_test_split(excel_data, 0.3)

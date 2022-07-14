#-*- coding:utf-8 -*-

import numpy as np
from scipy.stats import pearsonr

def bias_score(y_true, y_pred):
    '''
    '''
    mean_bias = np.mean(y_true - y_pred)
    #
    return mean_bias

def r_score(y_true, y_pred):
    '''
    '''
    r, p  = pearsonr(y_true, y_pred)
    #
    return r, p

def r2_score(y_true, y_pred, regression_type = "simple"):
    '''
    regression_type:simple,multiple
    '''
    if regression_type == "simple":
        r, _ = r_score(y_true, y_pred)
        r2 = r ** 2
    elif regression_type == "multiple":
##        sse = np.sum((y_true - y_pred) ** 2)
##        sst = np.sum((y_true - np.mean(y_true)) ** 2)
##        r2 = 1 - sse / sst
        r2 = sklearn_r2_score(y_true, y_pred)
    else:
        raise Exception("Invalid parameter 'regression_type',it must be simple or multiple.")
    #
    return r2

def mae_score(y_true, y_pred):
    '''
    '''
    n = np.shape(y_true)[0]
    if n != np.shape(y_pred)[0]:
        return None
    #
    mae = np.sum(np.abs(y_true - y_pred))/n
    #
    return mae

def mape_score(y_true, y_pred):
    '''
    '''
    n = np.shape(y_true)[0]
    if n != np.shape(y_pred)[0]:
        return None
    #
    mape = np.sum(np.abs((y_true - y_pred)/y_true)) / n * 100
    #
    return mape

def mse_score(y_true, y_pred):
    '''
    '''
    n = np.shape(y_true)[0]
    if n != np.shape(y_pred)[0]:
        return None
    #
    mse = np.sum(np.square(y_true - y_pred))/n
    #
    return mse

def rmse_score(y_true, y_pred):
    '''
    '''
    rmse = np.sqrt(mse_score(y_true, y_pred))
    #
    return rmse

if __name__ == "__main__":
    #
    y_true = np.random.rand(100)
##    y_pred = y_true
    y_pred = np.random.rand(100)
    #
    print(y_pred.shape)
    print(r_score(y_true, y_pred))
    print(r2_score(y_true, y_pred))
    print(mae_score(y_true, y_pred))
    print(mape_score(y_true, y_pred))
    print(mse_score(y_true, y_pred))
    print(rmse_score(y_true, y_pred))

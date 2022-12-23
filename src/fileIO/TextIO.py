# -*- coding:utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np


def is_bom_utf8(file_path):
    '''
    '''
    BOM_info = None
    with open(file_path, 'rb') as fid:
        BOM_info = fid.read(3)
        if BOM_info == b"\xef\xbb\xbf":
            return True
        else:
            return False

def read_csv(file_path):
    '''
    '''
    is_BOM_utf8 = is_bom_utf8(file_path)
    with open(file_path, 'rb') as fid:
        if is_BOM_utf8:
            fid.seek(3)
        data = np.loadtxt(fid, dtype = np.float64, delimiter = ',') 
    #
    return data      

def write_csv(file_path, data):
    '''
    '''
    with open(file_path, 'w') as fid:
        np.savetxt(fid, data, delimiter = ',', fmt=["%.18f"] * data.shape[1], encoding = "utf-8")


if __name__ == "__main__":
    #
    raise Exception(__file__ + " " + "The script can not be excuted alone!")
    #
##    data = read_csv(r"C:\Users\ruixi\Desktop\1.1.train_GOCI_TSS.csv")
##    print(data.shape)sss
##    print(data[0,:])
##    write_csv(r"C:\Users\ruixi\Desktop\1.1.train_GOCI_TSS_no_bom.csv", data)
##    print(read_csv(r"H:\Data\MLData\RegressionData\Chl-a数据\test_landsat_chla_1.csv"))

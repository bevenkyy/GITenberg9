# -*- coding: utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np

def image_fusion_STARFM(img1_T0, img1_Tk, img2_Tk, window_size = 15, constang_S = 1.0, constang_T = 1.0, constang_D = 1.0, constang_A = 4.0):
    '''
    '''
    img_height, img_width = img1_T0.shape
    #
    img2_T0 = np.zeros([img_height, img_width], dtype = np.float64)
    #
    S_ijk = np.abs(img1_Tk - img2_Tk)
    T_ijk = np.abs(img1_Tk - img1_T0)
    D_ijk = np.zeros([window_size, window_size], dtype = np.float64)
    center_XY_Index = int(np.ceil(window_size / 2.0)) - 1;
    #
    for j in range(window_size):
        for i in range(window_size):
            D_ijk[i, j] = 1.0 + np.sqrt((center_XY_Index - i) ** 2 + (center_XY_Index - j) ** 2) / constang_A
    #
    distance_to_edge = int(np.floor(window_size / 2.0));
    for j in range(distance_to_edge, img_width - distance_to_edge):
        for i in range(distance_to_edge, img_height - distance_to_edge):
            tmp_Sijk = S_ijk[i - distance_to_edge:i - distance_to_edge + window_size, j - distance_to_edge:j - distance_to_edge + window_size]
            tmp_Tijk = T_ijk[i - distance_to_edge:i - distance_to_edge + window_size, j - distance_to_edge:j - distance_to_edge + window_size]
            #
            C_ijk = (constang_S * tmp_Sijk) * (constang_T * tmp_Tijk) * (constang_D * D_ijk)
            #
            W_ijk = (1.0 / C_ijk)/np.sum(1 / C_ijk)
            #
            tmp_Img1T0 = img1_T0[i - distance_to_edge:i - distance_to_edge + window_size, j - distance_to_edge:j - distance_to_edge + window_size]
            tmp_Img2Tk = img2_Tk[i - distance_to_edge:i - distance_to_edge + window_size, j - distance_to_edge:j - distance_to_edge + window_size]
            tmp_Img1Tk = img1_Tk[i - distance_to_edge:i - distance_to_edge + window_size, j - distance_to_edge:j - distance_to_edge +window_size]
            img2_T0[i,j] = np.sum(W_ijk * (tmp_Img1T0 + tmp_Img2Tk - tmp_Img1Tk))
    #
    return img2_T0


if __name__ == "__main__":
    #
    pass

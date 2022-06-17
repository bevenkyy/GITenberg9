# -*-coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import shapefile as shpfile

with shpfile.Reader(r"C:\Users\lenovo\Desktop\CHN_adm_shp\CHN_adm1.shp") as shp:
    print(type(shp))

# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtWidgets

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GeoDataMap(FigureCanvas):
    '''
    '''
 
    def __init__(self):
        '''
        '''
        figure = self.plot_map()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()
        
 
    def plot_map(self):
        '''
        '''
        figure = Figure(figsize=(8, 8), dpi=100, facecolor="lightgray")
        axes = figure.add_axes([0.1,0.1,0.8,0.8])
        #
        basemap = Basemap()
        features = basemap.readshapefile(r"C:\Users\lenovo\Desktop\反演区域\L8_20180825_water","L8_20180825_water", ax = axes)
        print(type(features))
##        features = basemap.drawcoastlines()
        #
        return figure

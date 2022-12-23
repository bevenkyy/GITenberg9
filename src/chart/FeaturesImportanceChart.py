# -*- coding: utf-8 -*-

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtWidgets

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class FeaturesImportanceChart(FigureCanvas):
    '''
    '''
    data = None
    select_algorithm = None
 
    def __init__(self, data, select_algorithm):
        '''
        '''
        #
        self.data = data
        self.select_algorithm = select_algorithm
        ##
        #
        figure = self.plot_features_importance()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()
        
    def __prase_data(self):
        '''
        '''
        x = []
        y = []
        for key, value in self.data.items():
            x.append(key)
            y.append(value)
        #
        return x, y
        
 
    def plot_features_importance(self):
        '''
        '''
        #
        figure = Figure(figsize=(8, 8), dpi=100, facecolor="lightgray")
        #
        axes = figure.add_subplot(111,  facecolor = [0.9, 0.9, 0.9])
        axes.set_title("Features Importance", fontsize=12)
        # axes.set_xticks(rotation=30)
        axes.set_xlabel("Features")
        axes.set_ylabel("Pearson Correlation Coefficient")
##        axes1.set_xlim(0,50)
##        axes1.set_ylim(0,50)
        x, y = self.__prase_data()
        #
        axes.grid(True, axis='y', color=[1.0,1.0,1.0])
        #
        axes.bar(x, y, edgecolor="black")
        #
        figure.set_tight_layout(True)
        #
        return figure

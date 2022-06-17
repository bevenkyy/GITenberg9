# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2/Lib/site-packages"))
##sys.path.append(os.path.dirname(os.path.join(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2/python37.zip"))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PySide2 import QtCore, QtWidgets

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class HistgramChart(FigureCanvas):
    '''
    '''
    data = None
    bins = None
 
    def __init__(self, data, bins):
        '''
        '''
        #
        self.data = data
        self.bins = bins
        ##
        #
        figure = self.plot_hist()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()
        
 
    def plot_hist(self):
        '''
        '''
        #
        figure = Figure(figsize=(8, 8), dpi=100, facecolor="lightgray")
        #
        # =======================================================axes1=======================================================
        axes1 = figure.add_subplot(131)
        axes1.set_title("All Samples", fontsize=12)
##        axes1.set_xlabel("Measured Values(x)")
##        axes1.set_ylabel("Predicted Values(y)")
##        axes1.set_xlim(0,50)
##        axes1.set_ylim(0,50)
        axes1.hist(self.data[0], bins = self.bins, edgecolor="black")
        #
        # =======================================================axes2=======================================================
        axes2 = figure.add_subplot(132)
        axes2.set_title("Training-Validation Samples", fontsize=12)
##        axes2.set_xlabel("Measured Values(x)")
##        axes2.set_ylabel("Predicted Values(y)")
##        axes2.set_xlim(0,50)
##        axes2.set_ylim(0,50)
        axes2.hist(self.data[1], bins = self.bins, edgecolor="black")
        #
        # =======================================================axes3=======================================================
        axes3 = figure.add_subplot(133)
        axes3.set_title("Test Samples", fontsize=12)
##        axes3.set_xlabel("Measured Values(x)")
##        axes3.set_ylabel("Predicted Values(y)")
##        axes3.set_xlim(0,50)
##        axes3.set_ylim(0,50)
        axes3.hist(self.data[2], bins = self.bins, edgecolor="black")
        #
        figure.set_tight_layout(True)
        #
        return figure

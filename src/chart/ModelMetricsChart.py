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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ModelMetricsChart(FigureCanvas):
    '''
    '''
    y_true_train_val = None
    y_pred_train_val = None
    train_val_score = None
    y_true_test = None
    y_pred_test = None
    test_score = None
 
    def __init__(self, fitting_data, prediction_data):
        '''
        '''
        #
        self.y_true_train_val = fitting_data.get("y_true_train_val")
        self.y_pred_train_val = fitting_data.get("y_pred_train_val")
        self.train_val_score = fitting_data.get("score")
        self.y_true_test = prediction_data.get("y_true_test")
        self.y_pred_test = prediction_data.get("y_pred_test")
        self.test_score = prediction_data.get("score")
        #
        ##
        #
        figure = self.plot_metrics()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()
        
 
    def plot_metrics(self, xytick_range = (0,50)):
        '''
        '''
        max_train_xytick_value = max(int(np.ceil(np.max(self.y_true_train_val))), int(np.ceil(np.max(self.y_pred_train_val))))
        max_test_xytick_value = max(int(np.ceil(np.max(self.y_true_test))), int(np.ceil(np.max(self.y_pred_test))))
        #
        train_x = np.arange(0, max_train_xytick_value) # train:one divide-by one line
        test_x = np.arange(0, max_test_xytick_value) # test:one divide-by one line
        #
        train_val_slope, train_val_intercept = self.fitting_line_params(self.y_true_train_val, self.y_pred_train_val)
        train_val_plot_y = train_val_slope * train_x + train_val_intercept
        #
        test_slope, test_intercept = self.fitting_line_params(self.y_true_test, self.y_pred_test)
        test_plot_y = test_slope * test_x + test_intercept
        #
        figure = Figure(figsize=(8, 8), dpi=100, facecolor="lightgray")
        #
        # =======================================================axes1=======================================================
        axes1 = figure.add_subplot(121)
        axes1.set_title("$Training:R^2=$" + str(round(self.train_val_score, 4)), fontsize=12)
        axes1.set_xlabel("Measured Values(x)")
        axes1.set_ylabel("Predicted Values(y)")
        axes1.set_xlim(0, max(int(np.ceil(np.max(self.y_true_train_val))), int(np.ceil(np.max(self.y_pred_train_val)))))
        axes1.set_ylim(0,max(int(np.ceil(np.max(self.y_true_train_val))), int(np.ceil(np.max(self.y_pred_train_val)))))
        axes1.plot(train_x, train_x, color = "gray", linestyle = ":")
        axes1.scatter(self.y_true_train_val, self.y_pred_train_val, color = "", edgecolors = "black", marker = "o")
        axes1.plot(train_x,train_val_plot_y, color = "red", linestyle = "-")
        #
        # =======================================================axes2=======================================================
        axes2 = figure.add_subplot(122)
        axes2.set_title("$Test:R^2=$" + str(round(self.test_score, 4)), fontsize=12)
        axes2.set_xlabel("Measured Values(x)")
        axes2.set_ylabel("Predicted Values(y)")
        axes2.set_xlim(0,max(int(np.ceil(np.max(self.y_true_test))), int(np.ceil(np.max(self.y_pred_test)))))
        axes2.set_ylim(0,max(int(np.ceil(np.max(self.y_true_test))), int(np.ceil(np.max(self.y_pred_test)))))
        axes2.plot(test_x, test_x, color = "gray", linestyle = ":")
        axes2.scatter(self.y_true_test, self.y_pred_test, color = "", edgecolors = "black", marker = "o")
        axes2.plot(test_x, test_plot_y, color = "red", linestyle = "-")
        #
        figure.set_tight_layout(True)
        #
        return figure


    def fitting_line_params(self, true_value, prediction_value):
        '''
        '''
        x = true_value
        y = prediction_value
        n = x.shape[0]
        #
        slope = (np.sum(x * y) - (np.sum(x) * np.sum(y))/n)/ \
                (np.sum(x ** 2) - np.sum(x) ** 2/n)
        #
        intercept = np.mean(prediction_value) - slope * np.mean(prediction_value)
        #
        return slope, intercept

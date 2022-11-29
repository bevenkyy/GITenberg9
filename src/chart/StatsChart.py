# -*- coding: utf-8 -*-

import os
import sys
from collections import Counter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtWidgets
from scipy.stats import linregress

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")    #必须放在其他matplotlib引用之前
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
plt.rcParams["font.sans-serif"] = ["SimHei"] #用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False #用来正常显示负号

from MathLib.stats_score import *

class CoordinateAxis(FigureCanvas):
    '''
    '''
 
    def __init__(self, title = "Coordinate Axis", xlabel = "x", ylabel = "count", 
                 xlim = (0, 50), ylim = (0, 50), dpi=100, figsize = (8, 8), facecolor = (0.98,0.98,0.98)):
        '''
        '''
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.ylim = ylim
        self.dpi = dpi
        self.figsize = figsize
        self.facecolor = facecolor
        #
        figure = self.plot_axis()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()
        
 
    def plot_axis(self):
        '''
        '''
        #
        figure = Figure(figsize = self.figsize, dpi = self.dpi, facecolor = self.facecolor)
        #
        axes = figure.add_subplot(111)
        axes.set_title(self.title, fontsize = 12)
        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        axes.set_xlim(self.xlim)
        axes.set_ylim(self.ylim)
        #
        figure.set_tight_layout(True)
        #
        return figure

class LineChart(FigureCanvas):

    def __init__(self, data,
                 title = "line chart", xlabel = "x", ylabel = "value", xlim = (0, 2), ylim = (0, 2), 
                 dpi=100, figsize = (8, 8), face_color=(0.98,0.98,0.98), line_color = "#2E6D8E"):
        '''
        '''
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.ylim = ylim
        self.dpi = dpi
        self.figsize = figsize
        self.face_color = face_color
        self.line_color = line_color
        #
        figure = self.plot_line()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()

    def plot_line(self):
        figure = Figure(figsize = self.figsize, dpi = self.dpi, facecolor = self.face_color)
        #
        axes = figure.add_subplot(111)
        axes.set_title(self.title, fontsize = 12)
        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        # axes.set_xlim(self.xlim)
        # axes.set_ylim(self.ylim)
        axes.plot(np.arange(1, self.data.shape[0] + 1), self.data, color = self.line_color)
        #
        figure.set_tight_layout(True)
        #
        return figure

class BarChart(FigureCanvas):

    def __init__(self, data, legend,
                 title = "柱状图", xlabel = "class", ylabel = "value", tick_label = None, dpi=100, figure_size = (8, 8), 
                 facecolor=(0.98,0.98,0.98), edgecolor = (0.25,0.25,0.25)):
        '''
        '''
        self.data = data
        self.legend = legend
        #
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.tick_label = tick_label
        #
        self.figure_size = figure_size
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.dpi = dpi
        #
        figure = self.plot_bar()
        #
        FigureCanvas.__init__(self, figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()


    def plot_bar(self):
        '''
        '''
        figure = plt.figure(figsize = self.figure_size, dpi = self.dpi, facecolor = self.facecolor)
        # 
        axes = figure.add_subplot(111)
        axes.set_title(self.title, fontsize = 12)
        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        #
        # x = []
        # y = []
        # Counter的用法
        # for value, count in Counter(self.data).items():
        #     x.append(value)
        #     y.append(count)
        #
        bar_handles = []
        for i, (stat_value, legend) in enumerate(zip(self.data, self.legend)):
            x = tuple(map(lambda x: x + i * 0.3, [i for i in range(1, len(stat_value) + 1)]))
            y = stat_value
            handle = axes.bar(x, y, width = 0.3, tick_label = self.tick_label, label = legend)
            bar_handles.append(handle)
        #
        axes.legend(handles = bar_handles, loc='best')
        figure.set_tight_layout(True)
        #
        return figure

class HistgramChart(FigureCanvas):
    '''
    '''
 
    def __init__(self, data, bins = 50, 
                 title = "histogram chart", xlabel = "x", ylabel = "count", xlim = (0, 2), ylim = (0, 2), 
                 dpi=100, figsize = (8, 8), facecolor=(0.98,0.98,0.98), edgecolor = (0.25,0.25,0.25)):
        '''
        '''
        self.data = data
        self.bins = bins
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.ylim = ylim
        self.dpi = dpi
        self.figsize = figsize
        self.facecolor = facecolor
        self.edgecolor = edgecolor
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
        figure = Figure(figsize = self.figsize, dpi = self.dpi, facecolor = self.facecolor)
        #
        axes = figure.add_subplot(111)
        axes.set_title(self.title, fontsize = 12)
        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        # axes.set_xlim(self.xlim)
        # axes.set_ylim(self.ylim)
        axes.hist(self.data, bins = self.bins, edgecolor = self.edgecolor)
        #
        figure.set_tight_layout(True)
        #
        return figure

class EstimatorCurveChart(FigureCanvas):

    def __init__(self, training_size, training_scores, cv_scores):
        '''
        '''
        self.training_size = training_size
        self.training_scores = training_scores
        self.cv_scores = cv_scores
        #
        self._figure = self._plot_curve()
        #
        FigureCanvas.__init__(self, self._figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()

    def _plot_curve(self):
        '''
        '''
        figure = plt.figure(figsize = (5, 4), facecolor = "lightgray")
        #
        axes = figure.add_subplot(111)
        axes.tick_params(axis = "both", direction = "in", top = True, right = True)
        training_curve, = axes.plot(self.training_size, self.training_scores,
                                    'o-', color = "#003366",
                                    label = "Training score")
        cv_curve, = axes.plot(self.training_size, self.cv_scores,
                            'o-', color = "#FF9900",
                            label = "Cross-Validation score")
        #
        axes.set_xlabel("Training Size")
        axes.set_ylabel("MSE")
        axes.legend(handles=[training_curve, cv_curve],
                    loc='upper right')
        axes.grid(True)
        #
        return figure

    def get_figure(self):
        #
        return self._figure

class EstimatorScatterChart(FigureCanvas):
    
    def __init__(self, y_true, y_pred, title = "Scatter Chart", x_label = "X", y_label = "Y", axes_color = [0.9, 0.9, 0.9], 
                 marker = "o", marker_size = 100, edge_width = 1, edge_color = [0.2, 0.4, 0.7, 0.4], filling_color = [0.2, 0.4, 0.7, 0.4], 
                 figure_size = (8, 8), figure_color = [0.85, 0.85, 0.85], dpi = 100, show_grid = True,
                 fitting_line_color = (0.0, 0.0, 0.0, 1.0), 
                 one_one_line_color = "gray"):
        '''
        '''
        self.y_true = y_true
        self.y_pred = y_pred
        #
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.axes_color = axes_color
        #
        # self.marker = marker
        # self.marker_size = marker_size
        # self.edge_width = edge_width
        # self.edge_color = edge_color
        # self.filling_color = filling_color
        # #
        # self.figure_size = figure_size
        # self.figure_color = figure_color
        # self.dpi = dpi
        # self.show_grid = show_grid
        # #
        # self.fitting_line_color = fitting_line_color
        # self.one_one_line_color = one_one_line_color
        ##
        #
        #
        self._figure = self._plot_scatter()
        #
        FigureCanvas.__init__(self, self._figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()

    def calc_fitting_line(self):
        '''
        '''
        n = self.y_true.shape[0]
        #
        slope = (np.sum(self.y_true *  self.y_pred) - (np.sum(self.y_true) * np.sum( self.y_pred))/n)/ \
                (np.sum(self.y_true ** 2) - np.sum(self.y_true) ** 2/n)
        #
        intercept = np.mean(self.y_true) - slope * np.mean(self.y_pred)
        #
        return slope, intercept

    def _plot_scatter(self):
        '''
        '''
        slope, intercept = self.calc_fitting_line()
        self.y_fitting = self.y_true * slope + intercept
        #
        max_xytick_value = max(int(np.ceil(np.max(self.y_true))), int(np.ceil(np.max(self.y_pred))))
        x = np.arange(0, max_xytick_value + 1) # test:one divide-by one line
        #
        figure = plt.figure(figsize = (8.5, 8), facecolor = "lightgray")
        # 
        axes = figure.add_subplot(111)
        axes.tick_params(axis = "both", direction = "in", top = True, right = True)
        #
        axes.plot(x, x, color = "gray", linestyle = "--")
        axes.scatter(self.y_true, self.y_pred, 
                     color = "#003366",
                     edgecolors = "#003366",
                     marker = '+',
                     s = 75)
        axes.plot(self.y_true, self.y_fitting, color="red", linestyle = "-")
        #
        axes.set_xlim(0, max(int(np.ceil(np.max(self.y_true))), int(np.ceil(np.max(self.y_pred)))))
        axes.set_ylim(0,max(int(np.ceil(np.max(self.y_true))), int(np.ceil(np.max(self.y_pred)))))
        #
        axes.set_xlabel(self.x_label)
        axes.set_ylabel(self.y_label)
        axes.set_title(self.title)
        #
        figure.set_tight_layout(True)
        #
        return figure

    def get_figure(self):
        #
        return self._figure

class EstimatorConfusionMatrix(FigureCanvas):
    def __init__(self, y_true, y_pred, title = "Confusion Matrix", x_label = "True Class", y_label = "Pred Class", 
                 axes_color = [0.9, 0.9, 0.9], 
                 figure_size = (8, 8), figure_color = [0.85, 0.85, 0.85], dpi = 100):
        '''
        '''
        self.confusion_matrix, _ = calc_confusion_matrix(y_true, y_pred)
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.axes_color = axes_color
        #
        # self.figure_size = figure_size
        # self.figure_color = figure_color
        # self.dpi = dpi
        #
        self._figure = self._plot_ConfusionMatrix()
        #
        FigureCanvas.__init__(self, self._figure)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #
        self.draw()

    def _plot_ConfusionMatrix(self):
        '''
        '''
        figure = plt.figure(figsize = (8.5, 8), facecolor = "lightgray")
        # 
        axes = figure.add_subplot(111)
        #
        axes.imshow(self.confusion_matrix)
        #
        axes.set_title(self.title)
        axes.set_xlabel(self.x_label)
        axes.set_ylabel(self.y_label)
        # axes.set_xticklabels(row_labels, minor=False)
        # axes.set_yticklabels(column_labels, minor=False)
        # axes.set_xlim(0, max(int(np.ceil(np.max(self.y_true))), int(np.ceil(np.max(self.y_pred)))))
        # axes.set_ylim(0,max(int(np.ceil(np.max(self.y_true))), int(np.ceil(np.max(self.y_pred)))))
        # axes.tick_params(axis = "both", direction = "in", top = True, right = True)
        #
        figure.set_tight_layout(True)
        #
        return figure

    def get_figure(self):
        #
        return self._figure

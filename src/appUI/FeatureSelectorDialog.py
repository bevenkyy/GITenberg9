# -*- coding:utf-8 -*-

import os
import sys
from matplotlib.pyplot import title

from numpy.lib.function_base import append

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from fileIO import ExcelIO, ModelIO
from data.FeatureProcessor import calculate_variance, calculate_pearson_correlation, calculate_distance_correlation
from InitResource import get_icon

from chart.StatsChart import  CoordinateAxis, BarChart
from FeatureSelectorDialogDesigner import Ui_FeatureSelectorDialog

class FeatureSelectorDialog(QDialog, Ui_FeatureSelectorDialog):

    #
    qSetting = None
    #     
    sample = None
    feature_stats = {"variance":None,
                    "pearson_corrcoef":None,
                    "distance_corrcoef":None}

    def __init__(self, setting):
        super(FeatureSelectorDialog, self).__init__(None)
        self.setupUi(self)
        self.qSetting = setting
        #
        #
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #
        self.coordinateAxis = CoordinateAxis()
        self.significanceCharHorizontalLayout.addWidget(self.coordinateAxis)
        #
        # 临时禁用
        self.selectSalientFeatureComboBox.setEnabled(False)
        self.selectSaveSalientFeaturePushButton.setEnabled(False)
        self.selectSaveSalientFeatureLineEdit.setEnabled(False)
        #
        #========singal and slot========
        self.selectOpenDataFilePushButton.clicked.connect(self.selectOpenDataFilePushButtonClicked)
        self.selectSaveSalientFeaturePushButton.clicked.connect(self.selectSaveSalientFeaturePushButtonClicked)

    def selectOpenDataFilePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个数据文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectOpenDataFileLineEdit.setText(file_path)
            #
            self.sample = ExcelIO.read_excel(file_path).astype(np.float64)
            #
            variance_array = []
            pearson_corrcoef_array = []
            distance_corrcoef_array = []
            for j in range(self.sample.shape[1] - 1):
                variance_array.append(calculate_variance(self.sample[:,j]))
                pearson_corrcoef_array.append(calculate_pearson_correlation(self.sample[:,j], self.sample[:,-1]))
                distance_corrcoef_array.append(calculate_distance_correlation(self.sample[:,j], self.sample[:,-1]))
            #
            self.feature_stats = (variance_array, pearson_corrcoef_array, distance_corrcoef_array)
            self.legend = ["Variance","Pearson Correlation","Distance Correlation"]
            self.tick_label = ["Feature{}".format(i) for i in range(1, self.sample.shape[1])]
            self.barChart = BarChart(self.feature_stats, self.legend, tick_label = self.tick_label, title = "特征分布统计图")
            self.significanceCharHorizontalLayout.removeWidget(self.coordinateAxis)
            self.significanceCharHorizontalLayout.addWidget(self.barChart)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def selectSaveSalientFeaturePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存数据的文件名",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectSaveSalientFeatureLineEdit.setText(file_path)
            #
            if not self.isSaveSignificanceInfoCheckBox.isChecked():
                save_sample = self.sample
                row_title = [i + 1 for i in range(save_sample.shape[0])]
            else:
                save_sample = np.vstack([self.sample, 
                            self.feature_stats_info.get("variance"),
                            self.feature_stats_info.get("pearson_corrcoef"),
                            self.feature_stats_info.get("distance_corrcoef")])
                #
                row_title = [i + 1 for i in range(save_sample.shape[0] - 3)]
                row_title.append("variance")
                row_title.append("pearson_corrcoef")
                row_title.append("distance_corrcoef")
            col_title = ['F' + str(i + 1) for i in range(save_sample.shape[1] - 1)]
            col_title.insert(0, "ID")
            col_title.append("Label")
            ExcelIO.write_excel(file_path, ["FeatureSignificance",],[save_sample, ],
                                row_title=row_title,col_title=col_title)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))
            #
            if QMessageBox.information(self, "提示", "数据保存成功！", QMessageBox.Ok) == QMessageBox.Ok:
                self.close()


def main(setting):
    app = QApplication(sys.argv)
    featureSelectorDialog = FeatureSelectorDialog(setting)
    featureSelectorDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

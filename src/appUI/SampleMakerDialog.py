# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
import numpy as np

from InitResource import get_icon
from SampleMakerDialogDesigner import Ui_SampleMakerDialog
from fileIO import ExcelIO
from data import SampleMaker
from chart.StatsChart import CoordinateAxis, BarChart, HistgramChart


class SampleMakerDialog(QDialog, Ui_SampleMakerDialog):
    '''
    '''
    #
    qSetting = None
    #
    training_cv_samples = None
    test_samples = None


    def __init__(self, setting):
        super(SampleMakerDialog, self).__init__(None)
        self.setupUi(self)

        self.init_sample_distribution_chart()
        #
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #

        self.qSetting = setting
        #
        if self.isRegressorSamplesRadioButton.isChecked():
            self.sampleType = "classificationSample"
        else:
            self.sampleType = "regressionSample"
        #
        self.selectAllSamplePushButton.clicked.connect(self.selectAllSamplePushButtonClicked)
        self.saveTrainingCVSamplePushButton.clicked.connect(self.saveTrainingCVSamplePushButtonClicked)
        self.saveTestSamplePushButton.clicked.connect(self.saveTestSamplePushButtonClicked)
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
    
    def init_sample_distribution_chart(self):
        #
        self.training_cv_axis = CoordinateAxis(title="Training Cross Validation Samples")
        self.sampleDistributionChartGridLayout.addWidget(self.training_cv_axis, 0,0,1,1)
        self.test_axis = CoordinateAxis(title="Test Samples") 
        self.sampleDistributionChartGridLayout.addWidget(self.test_axis, 0,1,1,1)

    def selectAllSamplePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个测试总体样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectAllSampleLineEdit.setText(file_path)
            #
            if self.isIncludeRowTitleCheckBox.isChecked() and self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = True
                isIncludeColTitle = True
            if not self.isIncludeRowTitleCheckBox.isChecked() and self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = False
                isIncludeColTitle = True
            if self.isIncludeRowTitleCheckBox.isChecked() and not self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = True
                isIncludeColTitle = False
            if not self.isIncludeRowTitleCheckBox.isChecked() and not self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = False
                isIncludeColTitle = False
            #
            test_size = self.testSampleSizeDoubleSpinBox.value()
            #
            try:
                excel_data = ExcelIO.read_excel(file_path, 
                                                has_row_labels = isIncludeRowTitle,
                                                has_col_labels = isIncludeColTitle)
                #
                try:
                    # self.training_cv_samples, self.test_samples = SampleMaker.sklearn_trainval_test_split(excel_data.astype(np.float64), test_size)
                    self.training_cv_samples, self.test_samples = SampleMaker.trainval_test_split(excel_data.astype(np.float64), test_size)
                    #
                    self.training_cv_stats_Chart = HistgramChart(self.training_cv_samples[:,-1], 
                                                            title="Training Cross Validation Samples")
                    self.sampleDistributionChartGridLayout.removeWidget(self.training_cv_axis)
                    self.sampleDistributionChartGridLayout.addWidget(self.training_cv_stats_Chart, 0,0,1,1)
                    #
                    self.test_stats_Chart = HistgramChart(self.test_samples[:,-1], title="Test Samples") 
                    self.sampleDistributionChartGridLayout.removeWidget(self.test_axis)
                    self.sampleDistributionChartGridLayout.addWidget(self.test_stats_Chart, 0,1,1,1)
                except Exception as split_sample_err_info:
                    QMessageBox.critical(self, "错误", "创建样本时发生了错误！错误信息如下：\n" + str(split_sample_err_info), QMessageBox.Ok)
            except Exception as read_file_err_Info:
                QMessageBox.critical(self, "错误", "读取文件时发生了错误！错误信息如下：\n" + str(read_file_err_Info), QMessageBox.Ok)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def saveTrainingCVSamplePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存训练验证样本的文件名",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.saveTrainingCVSampleLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))
    
    def saveTestSamplePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存测试样本的文件名",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.saveTestSampleLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def okPushButtonClicked(self):
        save_training_cv_Sample_file_path = self.saveTrainingCVSampleLineEdit.text()
        save_test_Sample_file_path = self.saveTestSampleLineEdit.text()
        #
        if save_training_cv_Sample_file_path != "" and save_test_Sample_file_path != "":
            training_cv_row_title = []
            test_row_title = []
            training_cv_test_col_title = ["ID"]
            for i in range(self.training_cv_samples.shape[0]):
                training_cv_row_title.append(i + 1)
            for i in range(self.test_samples.shape[0]):
                test_row_title.append(i + 1)
            for i in range(self.training_cv_samples.shape[1] - 1):
                training_cv_test_col_title.append("F" + str(i + 1))
            training_cv_test_col_title.append("Label")
            #
            try:
                ExcelIO.write_excel(save_training_cv_Sample_file_path, 
                                    ["training_cv_set",], 
                                    [self.training_cv_samples,],
                                    row_title = training_cv_row_title, 
                                    col_title = training_cv_test_col_title)
                ExcelIO.write_excel(save_test_Sample_file_path,
                                    ["test_set",], 
                                    [self.test_samples,],
                                    row_title = test_row_title, 
                                    col_title = training_cv_test_col_title)
                #
                if QMessageBox.information(self,"提示","已成功保存样本文件!", QMessageBox.Ok) == QMessageBox.Ok:
                    self.close()
            except Exception as write_file_err_info:
                QMessageBox.critical(self, "错误", "保存文件时发生了错误！错误信息如下：\n" + str(write_file_err_info), QMessageBox.Ok)


    def cancelPushButtonClicked(self):
        #
        self.close()

def main(setting):
    app = QApplication(sys.argv)
    sampleMakerDialog = SampleMakerDialog(setting)
    sampleMakerDialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)
    

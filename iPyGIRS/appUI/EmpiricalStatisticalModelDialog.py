# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unicodedata

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem

from EmpiricalStatisticalModelDialogDesigner import Ui_EmpiricalStatisticalModelDialog
from InitResource import get_icon, get_pixmap, get_gif
from fileIO import ModelIO, ExcelIO
from model.EmpiricStats import EmpiricStats
from ChartViewDialog import ChartViewDialog

class EmpiricalStatisticalModelDialog(QDialog, Ui_EmpiricalStatisticalModelDialog):
    '''
    '''
    #
    qSetting = None
    model_application = []
    
    def __init__( self, setting):
        super(EmpiricalStatisticalModelDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.init_ui_element()
        self.connect_signal_slot()
        #
        self.qSetting = setting
        #
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
        #

    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("tool_ToolBoxTreeWidget"))
        #
        self.selectTrainingSamplesPushButton.setIcon(get_icon("open_file"))
        self.selectTestSamplesPushButton.setIcon(get_icon("open_file"))
        #
        self.fittedEquationTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.fittedEquationTableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.fittedEquationTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def call_model_metrics_chart(self, data):
        #
        chartViewDialog = ChartViewDialog(self.qSetting, data, chart_type = "estimator_scatter")
        chartViewDialog.exec_()

    def connect_signal_slot( self ):
        self.selectTrainingSamplesPushButton.clicked.connect(self.selectTrainingSamplesPushButtonClicked)
        self.selectTestSamplesPushButton.clicked.connect(self.selectTestSamplesPushButtonClicked)
        self.addEquationPushButton.clicked.connect(self.addEquationPushButtonClicked)
        self.delEquationPushButton.clicked.connect(self.delEquationPushButtonClicked)

        self.trainingTestPushButton.clicked.connect(self.trainingTestPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
        
    def selectTrainingSamplesPushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个训练验证样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectTrainingSamplesLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def selectTestSamplesPushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个测试样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectTestSamplesLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def addEquationPushButtonClicked(self):
        if self.unfittedEquationListWidget.currentItem() != None:
            tmp_selection_item = self.unfittedEquationListWidget.currentItem().text()
            for row_index in range(self.fittedEquationTableWidget.rowCount()):
                if self.fittedEquationTableWidget.item(row_index, 0) == None:
                    self.fittedEquationTableWidget.setItem(row_index, 0, QTableWidgetItem(tmp_selection_item))
                    break
                else:
                    if self.fittedEquationTableWidget.item(row_index, 0).text() == tmp_selection_item:
                        break
                    else:
                        if self.fittedEquationTableWidget.item(row_index, 0).text() == "":
                            self.fittedEquationTableWidget.setItem(row_index, 0, QTableWidgetItem(tmp_selection_item))
                            break

    def delEquationPushButtonClicked(self):
        self.fittedEquationTableWidget.removeRow(self.fittedEquationTableWidget.currentRow())
        self.fittedEquationTableWidget.setRowCount(self.fittedEquationTableWidget.rowCount() + 1)

    def trainingTestPushButtonClicked(self):
        training_samples = ExcelIO.read_excel(self.selectTrainingSamplesLineEdit.text(), True, True)
        test_samples = ExcelIO.read_excel(self.selectTestSamplesLineEdit.text(), True, True)
        #
        training_x = training_samples[:,0]
        training_y = training_samples[:,1]
        test_x = test_samples[:,0]
        test_y = test_samples[:,1]
        #
        model_out = []
        for row_index in range(self.fittedEquationTableWidget.rowCount()):
            if self.fittedEquationTableWidget.item(row_index, 0) != None:
                currentEquation = self.fittedEquationTableWidget.item(row_index, 0).text()
                currentParams = unicodedata.normalize('NFKC', self.fittedEquationTableWidget.item(row_index, 1).text().strip())
                if currentParams.endswith(','): 
                    currentParams = currentParams[:-1]
                if currentParams.startswith(','): 
                    currentParams = currentParams[1:]
                init_params = [float(value) for value in currentParams.split(',')]
                #
                empiricStats = EmpiricStats(currentEquation, init_params)
                empiricStats.fit(training_x, training_y)
                empiricStats.predict(test_x, test_y)
                #
                equation_data = empiricStats.get_equation_data()
                # model_out.append([model_info, fit_data, pred_data])
        #
        # self.call_model_metrics_chart(model_out)

    def cancelPushButtonClicked(self):
        self.close()

        
def main(setting):
    app = QApplication(sys.argv)
    empiricalStatisticalModelDialog = EmpiricalStatisticalModelDialog(setting)
    empiricalStatisticalModelDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

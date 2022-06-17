# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from fileIO import ExcelIO, ModelIO
from data.DataPreprocessor import min_max_scaler, standard_scaler
from InitResource import get_icon

from DataScalerDialogDesigner import Ui_DataScalerDialog

class DataScalerDialog(QDialog, Ui_DataScalerDialog):

    #
    qSetting = None
    #     

    def __init__(self, setting):
        super(DataScalerDialog, self).__init__(None)
        self.setupUi(self)
        self.qSetting = setting

        #
        self.init_ui_element()
        #
        #========singal and slot========
        self.isMinMaxScalerRadioButton.clicked.connect(self.isMinMaxScalerRadioButtonClicked)
        self.isStandardScalerRadioButton.clicked.connect(self.isStandardScalerRadioButtonClicked)
        self.selectOpenDataFilePushButton.clicked.connect(self.selectOpenDataFilePushButtonClicked)
        self.selectSaveDataFilePushButton.clicked.connect(self.selectSaveDataFilePushButtonClicked)
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
    
    def init_ui_element(self):
        self.setWindowIcon(get_icon("tool_ToolBoxTreeWidget"))

    def isMinMaxScalerRadioButtonClicked(self):
        #
        if self.isMinMaxScalerRadioButton.isChecked():
            self.minMaxScalerRangeLineEdit.setEnabled(True)
        else:
            self.minMaxScalerRangeLineEdit.setEnabled(False)

    def isStandardScalerRadioButtonClicked(self):
        #
        if self.isStandardScalerRadioButton.isChecked():
            self.minMaxScalerRangeLineEdit.setEnabled(False)
        else:
            self.minMaxScalerRangeLineEdit.setEnabled(True)

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
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def selectSaveDataFilePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存数据的文件名",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectSaveDataFileLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def okPushButtonClicked(self):
        #
        preprocessing_file_path = self.selectOpenDataFileLineEdit.text()
        save_file_path = self.selectSaveDataFileLineEdit.text()
        include_row_title = self.isIncludeRowTitleCheckBox.isChecked()
        include_col_title = self.isIncludeColTitleCheckBox.isChecked()
        #
        preprocessing_data = ExcelIO.read_excel(preprocessing_file_path,
                                                has_row_labels=include_row_title, 
                                                has_col_labels=include_col_title)
        X, y = preprocessing_data[:,:-1], preprocessing_data[:,-1].reshape(-1, 1)
        #
        scale_range = tuple([float(i) for i in self.minMaxScalerRangeLineEdit.text().split('~')])
        #
        if self.isMinMaxScalerRadioButton.isChecked():
            scale_data = min_max_scaler(X, scale_range)
            scale_data = np.hstack([scale_data, y])
        else:
            scale_data = standard_scaler(X)
            scale_data = np.hstack([scale_data, y])
        #
        row_title = [i + 1 for i in range(scale_data.shape[0])]
        col_title = ['F' + str(i + 1) for i in range(scale_data.shape[1] - 1)]
        col_title.insert(0, "ID")
        col_title.append("Label")
        #
        ExcelIO.write_excel(save_file_path, ["scale_data",], [scale_data,], 
                            row_title = row_title, col_title = col_title)
        #
        if QMessageBox.information(self,"提示","已成功保存归一化/标准化数据!", QMessageBox.Ok) == QMessageBox.Ok:
            self.close()

    def cancelPushButtonClicked(self):
        #
        self.close()


def main(setting):
    app = QApplication(sys.argv)
    dataScalerDialog = DataScalerDialog(setting)
    dataScalerDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

# -*- coding:utf-8 -*-

import os
import sys
import re
from multiprocessing import Process, Manager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import numexpr as ne
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from fileIO import ExcelIO, RasterImgIO
from data.FeatureProcessor import calculate_variance, calculate_pearson_correlation, calculate_distance_correlation
from InitResource import get_icon, get_pixmap, get_gif

from FormulaApplicationDialogDesigner import Ui_FormulaApplicationDialog

class FormulaApplicationDialog(QDialog, Ui_FormulaApplicationDialog):

    def __init__(self, setting):
        super(FormulaApplicationDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        self.qTranslate = QtCore.QCoreApplication.translate
        #
        self.file_list = []
        self.formula_data = {}
        #
        self.init_ui_element()
        self.connect_signal_slot()

    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("tool_ToolBoxTreeWidget"))
        self.checkFormulaPushButton.setIcon(get_icon("checkError"))
        #
        self.selectDataFilePushButton.setIcon(get_icon("open_file"))
        self.delDataFilePushButton.setIcon(get_icon("del_file"))
        self.clearDataFilePushButton.setIcon(get_icon("clear_file"))
        #
        self.delVarPushButton.setIcon(get_icon("del_file"))
        self.clearVarPushButton.setIcon(get_icon("clear_file"))
        #
        self.fileListTableWidget.setHorizontalHeaderLabels(("待计算数据文件", "结果数据文件"))
        self.fileListTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) 
        self.fileListTableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.fileListTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.fileListTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #
        self.variableSettingTableWidget.setHorizontalHeaderLabels(("变量名", "变量取值"))
        self.variableSettingTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) 
        self.variableSettingTableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.variableSettingTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.variableSettingTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #
        # self.statusProgressBar.setValue = 0
        self.statusProgressBar.setVisible(False)
        self.statusTipLabel.setVisible(False)

    def connect_signal_slot(self):
        #
        self.selectDataFilePushButton.clicked.connect(self.selectDataFilePushButtonClicked)
        self.delDataFilePushButton.clicked.connect(self.delDataFilePushButtonClicked)
        self.clearDataFilePushButton.clicked.connect(self.clearDataFilePushButtonClicked)
        self.checkFormulaPushButton.clicked.connect(self.checkFormulaPushButtonClicked)

        self.delVarPushButton.clicked.connect(self.delVarPushButtonClicked)
        self.clearVarPushButton.clicked.connect(self.clearVarPushButtonClicked)

        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)

    def selectDataFilePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path_list, _ =  QFileDialog.getOpenFileNames(self, "打开一个或多个待预测的数据文件",
                                                          lastFileDir,
                                                          "GeoTiff文件(*.tif *.TIF);;Excel文件(*.xlsx)")
        if len(file_path_list) > 0:
            #
            for i, file_path in enumerate(file_path_list):
                if i + 1 > self.fileListTableWidget.rowCount():
                    self.fileListTableWidget.setRowCount(self.parameterListTableWidget.rowCount() + 5)
                for row_index in range(self.fileListTableWidget.rowCount()):
                    if self.fileListTableWidget.item(row_index, 0) == None:
                        self.fileListTableWidget.setItem(row_index, 0, QTableWidgetItem(file_path))
                        out_file_path = os.path.splitext(file_path)[0] + "_calc_" + str(row_index + 1) + os.path.splitext(file_path)[1]
                        self.fileListTableWidget.setItem(row_index, 1, QTableWidgetItem(out_file_path))
                        #
                        self.file_list.append((file_path, out_file_path))
                        #
                        break
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path_list[0]))
                    
    def delDataFilePushButtonClicked(self):
        self.fileListTableWidget.removeRow(self.fileListTableWidget.currentRow())
        self.fileListTableWidget.setRowCount(self.fileListTableWidget.rowCount() + 1)

    def clearDataFilePushButtonClicked(self):
        self.fileListTableWidget.clearContents()

    def selectSaveDirPushButtonClicked(self):
        pass

    def checkFormulaPushButtonClicked(self):
        self.formula_expression = self.inputFormulaLineEdit.text()
        if self.formula_expression == "":
            QMessageBox.critical(self, "错误", "无效的计算方程（方程中的变量必须属于26个大写字母）", QMessageBox.Ok)
            return
        else:
            formula_var = re.findall("[A-Z]", self.formula_expression)
            #
            for i, var in enumerate(formula_var):
                item = QTableWidgetItem(self.qTranslate("FormulaApplicationDialog", var))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.variableSettingTableWidget.setItem(i, 0, item)

    def delVarPushButtonClicked(self):
        self.variableSettingTableWidget.removeRow(self.variableSettingTableWidget.currentRow())
        self.variableSettingTableWidget.setRowCount(self.variableSettingTableWidget.rowCount() + 1)

    def clearVarPushButtonClicked(self):
        self.variableSettingTableWidget.clearContents()

    def okPushButtonClicked(self):
        self.checkFormulaPushButton.setEnabled(False)
        self.okPushButton.setEnabled(False)
        #
        self.statusProgressBar.setVisible(True)
        self.statusTipLabel.setVisible(True)
        self.statusTipLabel.setText("程序开始运行，共" +  str(len(self.file_list)) + "个待处理文件")
        #
        for row_index in range(self.variableSettingTableWidget.rowCount()):
            if self.variableSettingTableWidget.item(row_index,0) is not None:
                formula_var_name = self.variableSettingTableWidget.item(row_index,0).text()
                formula_var_expression = self.variableSettingTableWidget.item(row_index,1).text()
                formula_var_data = None
                #
                self.formula_data[formula_var_name] = (formula_var_expression, formula_var_data)
        #
        self.running_thread = RunFormulaCalcThread(self.file_list, self.formula_expression, self.formula_data)
        # self.running_thread.daemon = True #设置为守护线程
        self.running_thread.update_status_signal.connect(self.update_status)
        self.running_thread.start()  
    
    def update_status(self, current_status):
        self.statusTipLabel.setText("共" + str(current_status[0]) + 
                                    "个文件，正在处理第" + str(current_status[1]) + "个文件，请稍后……")
        self.statusProgressBar.setValue(current_status[2])
        if current_status[3] is not None:
            self.running_thread.thread_stop = True
            self.running_thread.quit()
            QMessageBox.critical(self,"错误","程序发生错误，信息如下：" + str(current_status[3]) + "请检查输入数据或向开发者反馈此问题！", 
                                 QMessageBox.Ok)
            self.close()
            return
        if current_status[2] == 100:
            #
            if QMessageBox.information(self,"提示","所有文件已处理完成!", QMessageBox.Ok) == QMessageBox.Ok:
                self.close()

    def cancelPushButtonClicked(self):
        self.close()
        

class RunFormulaCalcThread(QtCore.QThread):

    update_status_signal = QtCore.pyqtSignal(tuple)
    #
    thread_stop = False

    def __init__(self, file_list, formula_expression, formula_data):
        super().__init__()
        #
        self.file_list = file_list
        self.formula_expression = formula_expression
        self.formula_data = formula_data

    def _include_char(self, string, chars):
        '''
        '''
        is_include_char = False
        #
        for char in chars:
            if char in string:
                is_include_char = True
                break
            else:
                is_include_char = False
        #
        return is_include_char

    def run(self):
        #
        std_chars = ('+', '-', '*', '/')
        error_info = None
        #
        calc_formula_data = {}
        #
        image_file_count = len(self.file_list)
        #
        for i, (in_file, out_file) in enumerate(self.file_list):
            if self.thread_stop:
                break
            try:
                in_img = RasterImgIO.read_geotiff(in_file)
                img_info = RasterImgIO.query_geotiff_info(in_file)
                crs = img_info.get("crs")
                transform = img_info.get("transform")
                #
                for var_name, var_values in self.formula_data.items():
                    var_value_expression = var_values[0]
                    #
                    is_include_char = self._include_char(var_value_expression, std_chars)
                    if is_include_char:
                        var_value = ne.evaluate(var_value_expression,
                                                local_dict = in_img)
                    else:
                        var_value = in_img.get(var_value_expression)
                    #
                    calc_formula_data[var_name] = var_value
                #
                out_img = ne.evaluate(self.formula_expression, local_dict = calc_formula_data) 
                RasterImgIO.write_single_band(out_file, out_img, crs, transform)
            except Exception as error:
                error_info = error
            finally:
                status_percent = int((i + 1)/image_file_count * 100)
                if status_percent >= 99:
                    status_percent = 99
                self.update_status_signal.emit((image_file_count, i + 1, status_percent, error_info))
        #
        if self.thread_stop == False:
            self.update_status_signal.emit((image_file_count, image_file_count, 100, error_info))

def main(setting):
    app = QApplication(sys.argv)
    formulaApplicationDialog = FormulaApplicationDialog(setting)
    formulaApplicationDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

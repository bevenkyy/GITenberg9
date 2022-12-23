# -*- coding:utf-8 -*-

import os
import sys

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from fileio import ExcelIO, RasterImgIO, ModelIO
from data.DataPreprocessor import min_max_scaler, standard_scaler
from raster.BandCalculator import band_calc
from BandCalculatorDialogDesigner import Ui_BandCalculatorDialog
from utils.icons import get_icon


class BandCalculatorDialog(QDialog, Ui_BandCalculatorDialog):

    def __init__(self, setting):
        super(BandCalculatorDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        self.image_file_list = []
        self.valid_calc_formula = []
        self.save_band_order = []
        #
        self.init_ui_element()
        #
        #========singal and slot========
        self.connect_signal_slot()

    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #
        self.selectImageFilePushButton.setIcon(get_icon("open_file"))
        self.deleteImageFilePushButton.setIcon(get_icon("del_file"))
        self.clearImageFilePushButton.setIcon(get_icon("clear_file"))
        #
        self.deleteBandCalculationFormulaPushButton.setIcon(get_icon("del_file"))
        self.moveUpBandPushButton.setIcon(get_icon("move_up"))
        self.moveDownBandPushButton.setIcon(get_icon("move_down"))
        self.deleteBandPushButton.setIcon(get_icon("del_file"))
        self.clearBandCalculationFormulaPushButton.setIcon(get_icon("clear_file"))
        self.resetBandPushButton.setIcon(get_icon("reset_parameter"))
        self.selectSaveDirectoryPushButton.setIcon(get_icon("select_folder"))
        #
        self.fileListTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fileListTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.fileListTableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        #
        self.moveUpBandPushButton.setEnabled(False)
        self.moveDownBandPushButton.setEnabled(False)
        self.resetBandPushButton.setEnabled(False)

    def connect_signal_slot( self ):
        self.selectImageFilePushButton.clicked.connect(self.selectImageFilePushButtonClicked)
        self.deleteImageFilePushButton.clicked.connect(self.deleteImageFilePushButtonClicked)
        self.clearImageFilePushButton.clicked.connect(self.clearImageFilePushButtonClicked)
        self.addBandCalculationFormulaPushButton.clicked.connect(self.addBandCalculationFormulaPushButtonClicked)
        self.deleteBandCalculationFormulaPushButton.clicked.connect(self.deleteBandCalculationFormulaPushButtonClicked)
        self.clearBandCalculationFormulaPushButton.clicked.connect(self.clearBandCalculationFormulaPushButtonClicked)

        self.moveUpBandPushButton.clicked.connect(self.moveUpBandPushButtonClicked)
        self.moveDownBandPushButton.clicked.connect(self.moveDownBandPushButtonClicked)
        self.deleteBandPushButton.clicked.connect(self.deleteBandPushButtonClicked)
        self.resetBandPushButton.clicked.connect(self.resetBandPushButtonClicked)

        self.selectSaveDirectoryPushButton.clicked.connect(self.selectSaveDirectoryPushButtonClicked)

        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)

    def selectImageFilePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path_list, _ =  QFileDialog.getOpenFileNames(self, "选择一个或多个栅格影像文件",
                                                          lastFileDir,
                                                          "GeoTiff file(*.tif *.TIF)")
        if len(file_path_list) >= 1:
            for i, file_path in enumerate(file_path_list):
                if i + 1 > self.fileListTableWidget.rowCount():
                    self.fileListTableWidget.setRowCount(self.parameterListTableWidget.rowCount() + 5)
                for row_index in range(self.fileListTableWidget.rowCount()):
                    if self.fileListTableWidget.item(row_index, 0) == None:
                        self.fileListTableWidget.setItem(row_index, 0, QTableWidgetItem(file_path))
                        out_file_name = os.path.basename(os.path.splitext(file_path)[0] + "_calc" + os.path.splitext(file_path)[1])
                        self.fileListTableWidget.setItem(row_index, 1, QTableWidgetItem(out_file_name))
                        #
                        self.image_file_list.append([file_path, out_file_name])
                        #
                        break
            #
            valid_raster_band = RasterImgIO.query_valid_band(self.fileListTableWidget.item(0,0).text())
            self.validBandLineEdit.setText(valid_raster_band)
            #
            self.save_band_order.extend(valid_raster_band.split(','))
            self.saveBandOrderListWidget.addItems(self.save_band_order)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path_list[0]))

    def deleteImageFilePushButtonClicked(self):
        #
        if self.fileListTableWidget.currentRow() >= 0:  ##find a bug!!!!
            del self.image_file_dir[self.fileListTableWidget.currentRow()]
            self.fileListTableWidget.removeRow(self.fileListTableWidget.currentRow())
            self.fileListTableWidget.setRowCount(self.fileListTableWidget.rowCount() + 1)

    def clearImageFilePushButtonClicked(self):
        self.fileListTableWidget.clearContents()

    def addBandCalculationFormulaPushButtonClicked(self):
        std_chars = ['B', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                     '+', '-', '*', '/', '(', ')', ',', ' ']
        #
        calc_formula_text = self.bandCalculationFormulaLineEdit.text()
        if calc_formula_text != '':
            #
            if calc_formula_text.startswith(',') or calc_formula_text.endswith(','):
                QMessageBox.critical(self, "错误", "无效的计算公式，多个公式不能以逗号（,）开头或结尾", QMessageBox.Ok)
                return
            #
            for calc_formula_char in calc_formula_text:
                if calc_formula_char not in std_chars:
                    QMessageBox.critical(self, "错误", "无效的计算公式，公式中存在无效的字符", QMessageBox.Ok)
                    return
            #
            if ',' in calc_formula_text:
                for calc_formula_str in calc_formula_text.split(','):
                    if calc_formula_str not in self.valid_calc_formula:
                        self.valid_calc_formula.append(calc_formula_str)
                        #
                        self.validBandCalculationFormulaListWidget.clear()
                        self.validBandCalculationFormulaListWidget.addItems(self.valid_calc_formula)
                        #
                        if calc_formula_str not in self.save_band_order:
                            self.save_band_order.append(calc_formula_str)
                            #
                            self.saveBandOrderListWidget.clear()
                            self.saveBandOrderListWidget.addItems(self.save_band_order)
            else:
                calc_formula_str = calc_formula_text
                if calc_formula_str not in self.valid_calc_formula:
                    self.valid_calc_formula.append(calc_formula_str)
                    #
                    self.validBandCalculationFormulaListWidget.clear()
                    self.validBandCalculationFormulaListWidget.addItems(self.valid_calc_formula)
                    #
                    if calc_formula_str not in self.save_band_order:
                        self.save_band_order.append(calc_formula_str)
                        #
                        self.saveBandOrderListWidget.clear()
                        self.saveBandOrderListWidget.addItems(self.save_band_order)

    def deleteBandCalculationFormulaPushButtonClicked(self):
        current_item = self.validBandCalculationFormulaListWidget.currentItem()
        if current_item != None:
            current_item_text = self.validBandCalculationFormulaListWidget.currentItem().text()
            self.valid_calc_formula.remove(current_item_text)
        #
        self.validBandCalculationFormulaListWidget.clear()
        self.validBandCalculationFormulaListWidget.addItems(self.valid_calc_formula)

    def clearBandCalculationFormulaPushButtonClicked(self):
        self.valid_calc_formula = []
        self.validBandCalculationFormulaListWidget.clear()

    def moveUpBandPushButtonClicked(self):
        pass

    def moveDownBandPushButtonClicked(self):
        pass

    def deleteBandPushButtonClicked(self):
        selected_items = self.saveBandOrderListWidget.selectedItems()
        # Python浅拷贝、深拷贝，值类型和引用类型，for循环为遍历操作，对值类型操作无效，
        # 建议使用while循环代替，具体可参照网站：
        # https://www.jianshu.com/p/e20c78153299
        for selected_item in selected_items:
            current_text = selected_item.text()
            self.save_band_order.remove(current_text)
        #
        # i = 0
        # while i < len(selected_items):
        #     current_text = selected_items[i].text()
        #     self.save_band_order.remove(current_text)
        #     i += 1
        #
        self.saveBandOrderListWidget.clear()
        self.saveBandOrderListWidget.addItems(self.save_band_order)

    def resetBandPushButtonClicked(self):
        pass

    def selectSaveDirectoryPushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_dir =  QFileDialog.getExistingDirectory(self, "选择计算栅格文件的保存路径",
                                                     lastFileDir)
        if file_dir != "":
            self.selectSaveDirectoryLineEdit.setText(file_dir)
            for i, (_, out_file_name) in enumerate(self.image_file_list):
                self.image_file_list[i][1] = os.path.join(self.selectSaveDirectoryLineEdit.text(), out_file_name)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_dir))

    def okPushButtonClicked(self):
        if len(self.valid_calc_formula) < 1:
            QMessageBox.critical(self, "错误", "当前没有任何有效的计算公式，请至少输入一个计算公式", QMessageBox.Ok)
        else:
            band_calc(self.valid_calc_formula, self.image_file_list)
        #
        QMessageBox.information(self, "提示", "完成波段计算", QMessageBox.Ok)
        self.close()


    def cancelPushButtonClicked(self):
        #
        self.close()


def main(setting):
    app = QApplication(sys.argv)
    bandCalculatorDialog = BandCalculatorDialog(setting)
    bandCalculatorDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)




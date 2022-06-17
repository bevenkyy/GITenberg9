# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem

import logging
import numpy as np
from InitResource import get_icon
from PixelValueExtractorDialogDesigner import Ui_PixelValueExtractorDialog
from fileIO import ExcelIO, RasterImgIO
from raster import PixelValueExtractor 

class PixelValueExtractorialog(QDialog, Ui_PixelValueExtractorDialog):

    #
    image_file_dir = []
    coordinate_array = None

    def __init__(self, setting):
        super(PixelValueExtractorialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        #
        self.init_ui_element()
        self.connect_signal_slot()
    
    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("tool_ToolBoxTreeWidget"))
        #
        self.selectImageFilePushButton.setIcon(get_icon("open_file"))
        self.delImageFilePushButton.setIcon(get_icon("del_file"))
        self.clearImageFilePushButton.setIcon(get_icon("clear_file"))
        self.selectCoordinateFilePushButton.setIcon(get_icon("open_file"))
        self.selectSaveDirPushButton.setIcon(get_icon("select_folder"))
        #
        self.fileListTableWidget.setHorizontalHeaderLabels(("影像文件", "像元值文件"))
        self.fileListTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) 
        self.fileListTableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.fileListTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.fileListTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        #
        self.progressTipLabel.setVisible(False)
        self.progressTipProgressBar.setVisible(False)

    def connect_signal_slot(self):
        self.selectCoordinateFilePushButton.clicked.connect(self.selectCoordinateFilePushButtonClicked)
        self.selectImageFilePushButton.clicked.connect(self.selectImageFilePushButtonClicked)
        self.delImageFilePushButton.clicked.connect(self.delImageFilePushButtonClicked)
        self.clearImageFilePushButton.clicked.connect(self.clearImageFilePushButtonClicked)
        self.selectSaveDirPushButton.clicked.connect(self.selectSaveDirPushButtonClicked)
        #
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
    
    def selectCoordinateFilePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个像元值坐标文件",
                                                    lastFileDir,
                                                    "Excel file(*.xlsx)")
        if file_path != "":
            self.selectCoordinateFileLineEdit.setText(file_path)
            coordinate_filename = self.selectCoordinateFileLineEdit.text()
            #
            worksheet_names = ExcelIO.query_excel_info(coordinate_filename)
            worksheet_names = ExcelIO.query_excel_info(coordinate_filename)
            self.workSheetComboBox.clear()
            self.workSheetComboBox.addItems(worksheet_names)
            #
            excel_field = ExcelIO.read_excel_row(coordinate_filename, row_index = 0)
            #
            self.xFieldComboBox.clear()
            self.yFieldComboBox.clear()
            #
            self.xFieldComboBox.addItems(excel_field.tolist())
            self.yFieldComboBox.addItems(excel_field.tolist())
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def selectImageFilePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path_list, _ =  QFileDialog.getOpenFileNames(self, "选择一个或多个影像文件",
                                                          lastFileDir,
                                                          "GeoTiff file(*.tif *.TIF);;All file(*)")
        if len(file_path_list) >= 1:
            self.image_file_dir.append(os.path.dirname(file_path_list[0]))
            self.image_file_dir *= len(file_path_list)
            self.delImageFilePushButton.setEnabled(True)
            self.clearImageFilePushButton.setEnabled(True)
            if self.fileListTableWidget.rowCount() < len(file_path_list):
                self.fileListTableWidget.setRowCount(len(file_path_list))
            for file_path in file_path_list:
                for row_index in range(self.fileListTableWidget.rowCount()):
                    if self.fileListTableWidget.item(row_index, 0) == None:
                        self.fileListTableWidget.setItem(row_index, 0, 
                                                         QTableWidgetItem(os.path.basename(file_path)))
                        tmp_name = os.path.basename(file_path)
                        out_file_name = tmp_name[:-4]+ "_PixelValue.xlsx"
                        self.fileListTableWidget.setItem(row_index, 1, 
                                                         QTableWidgetItem(out_file_name))
                        break
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path_list[0]))
            
    def delImageFilePushButtonClicked(self):
        if self.fileListTableWidget.currentRow() >= 0:  ##find a bug!!!!
            del self.image_file_dir[self.fileListTableWidget.currentRow()]
            self.fileListTableWidget.removeRow(self.fileListTableWidget.currentRow())
            self.fileListTableWidget.setRowCount(self.fileListTableWidget.rowCount() + 1)
    
    def clearImageFilePushButtonClicked(self):
        self.image_file_dir = []
        self.fileListTableWidget.clearContents()
    
    def selectSaveDirPushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_dir =  QFileDialog.getExistingDirectory(self, "选择像元值文件的保存路径",
                                                     lastFileDir)
        if file_dir != "":
            self.selectSaveDirLineEdit.setText(file_dir)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_dir))
            
    def get_tableWidget_contents_count(self):
        #
        tableWidget_contents_count = 0
        for row_index in range(self.fileListTableWidget.rowCount()):
            if self.fileListTableWidget.item(row_index, 0) != None:
                tableWidget_contents_count += 1
            else:
                break
        #
        return tableWidget_contents_count

    def okPushButtonClicked(self):
        #
        self.progressTipLabel.setVisible(True)
        self.progressTipProgressBar.setVisible(True)
        self.okPushButton.setEnabled(False)
        self.progressTipLabel.setText("程序开始运行……")
        #
        if self.coordinateTypeComboBox.currentIndex() == 0:
            coordinates_type = "lonlat"
        elif self.coordinateTypeComboBox.currentIndex() == 1:
            coordinates_type = "xy"
        else:
            coordinates_type = "rowcol"
        #
        self.image_file_list = []
        self.pixel_value_file_list = []
        coordinate_filename = self.selectCoordinateFileLineEdit.text()
        worksheet_name = self.workSheetComboBox.currentText()
        xField = self.xFieldComboBox.currentText()
        yField = self.yFieldComboBox.currentText()
        pixel_radius = int(self.pixelRadiusSpinBox.text())
        noData = int(self.noDataLineEdit.text())
        invalidPixel = int(self.invalidPixelLineEdit.text())
        #
        for i in range(self.get_tableWidget_contents_count()):
            self.image_file_list.append(os.path.join(self.image_file_dir[i], 
                                                     self.fileListTableWidget.item(i, 0).text()))
            self.pixel_value_file_list.append(os.path.join(self.selectSaveDirLineEdit.text(), 
                                                           self.fileListTableWidget.item(i, 1).text()))
        #
        self.pixel_value_extractor_thread = RunThread(coordinates_type, coordinate_filename, worksheet_name, xField, yField,
                                                    self.image_file_list, self.pixel_value_file_list, 
                                                    pixel_radius, noData, invalidPixel)
        self.pixel_value_extractor_thread.updateFinishedStatus_signal.connect(self.updateFinishedStatus)
        self.pixel_value_extractor_thread.start()  

    def updateFinishedStatus(self, currentStatus):
        self.progressTipLabel.setText("程序工作进度：共" + str(currentStatus[0]) + 
                                      "个文件，正在提取第" + str(currentStatus[1]) + "个文件的像元值……")
        self.progressTipProgressBar.setValue(currentStatus[2])
        if currentStatus[2] == 100:
            #
            if QMessageBox.information(self,"提示","已完成像元值提取!", QMessageBox.Ok) == QMessageBox.Ok:
                self.close()
    
    def cancelPushButtonClicked(self):
        self.close()


class RunThread(QtCore.QThread):

    updateFinishedStatus_signal = QtCore.pyqtSignal(tuple)

    def __init__(self, coordinate_type, coordinate_filename, worksheet_name, xField, yField, 
                 image_file_list, pixel_value_file_list, 
                 pixel_radius, noData, invalidPixel):
        super().__init__()
        #
        self.coordinate_type = coordinate_type
        self.coordinate_filename = coordinate_filename
        self.worksheet_name = worksheet_name
        self.xField = xField
        self.yField = yField
        #
        self.image_file_list = image_file_list
        self.pixel_value_file_list = pixel_value_file_list
        #
        self.pixel_radius = pixel_radius
        self.noData = noData
        self.invalidPixel = invalidPixel

    def read_coordinate(self):
        #
        coordinate_array = None
        #
        xIndex = ExcelIO.query_field_index(self.coordinate_filename, self.worksheet_name, self.xField)
        yIndex = ExcelIO.query_field_index(self.coordinate_filename, self.worksheet_name, self.yField)
        excel_data = ExcelIO.read_excel(self.coordinate_filename, ws_name = self.worksheet_name)
        coordinate_array = np.hstack((excel_data[:,xIndex - 1].reshape(-1,1).astype(np.float64), 
                                    excel_data[:, yIndex - 1].reshape(-1,1).astype(np.float64)))
        #
        return coordinate_array

    def parse_coordinate(self, coordinate_array, geotiff_info):
        #
        all_lonlat_coordinate_array = all_colrow_coordinate_array = None
        #
        gcs = geotiff_info.get("gcs")
        pcs = geotiff_info.get("pcs")
        geotransform = geotiff_info.get("geotransform")
        #
        colrow_coordinate_array = np.zeros_like(coordinate_array, dtype = int)
        all_colrow_coordinate_array = np.zeros([(2 * self.pixel_radius + 1) ** 2 * coordinate_array.shape[0], coordinate_array.shape[1]],
                                            dtype = int)
        #
        if self.coordinate_type == "lonlat":
            for i, coordinates in enumerate(coordinate_array):
                col, row = PixelValueExtractor.lonlat_to_rowcol(gcs, pcs, geotransform, coordinates[0], coordinates[1])
                colrow_coordinate_array[i, 0] = col
                colrow_coordinate_array[i, 1] = row
        if self.coordinate_type == "xy":
            for i, coordinates in enumerate(coordinate_array):
                col, row = PixelValueExtractor.xy_to_rowcol(geotransform, coordinates[0], coordinates[1])
                colrow_coordinate_array[i, 0] = col
                colrow_coordinate_array[i, 1] = row
        #
        if self.pixel_radius > 0:
            for i, coordinates in enumerate(colrow_coordinate_array):
                tmp_rowcol_coordinate_list = []
                for col in range(coordinates[0] - self.pixel_radius, coordinates[0] + self.pixel_radius + 1):
                    for row in range(coordinates[1] - self.pixel_radius, coordinates[1] + self.pixel_radius + 1):
                        tmp_rowcol_coordinate_list.append([col, row])
                #
                all_colrow_coordinate_array[(2 * self.pixel_radius + 1) ** 2 * i:(2 * self.pixel_radius + 1) ** 2 * (i + 1),:] = tmp_rowcol_coordinate_list
            #
            all_lonlat_coordinate_array = np.zeros_like(all_colrow_coordinate_array, dtype = np.float64)
            for j, coordinate in enumerate(all_colrow_coordinate_array):
                #coordinate[1] is X(Horizontal)direction， coordinate[0] is Y(Vertical) direction
                all_lonlat_coordinate_array[j,:] = PixelValueExtractor.rowcol_to_lonlat(gcs, pcs, geotransform, coordinate[0], coordinate[1])
        else:
            all_colrow_coordinate_array = colrow_coordinate_array
            all_lonlat_coordinate_array = coordinate_array

        #
        return all_lonlat_coordinate_array, all_colrow_coordinate_array

    def run(self):
        #
        coordinate_array = self.read_coordinate()
        #
        geotiff_info = PixelValueExtractor.query_geotiff_info(self.image_file_list[0])
        lonlat_coordinate_array, colrow_coordinate_array = self.parse_coordinate(coordinate_array, geotiff_info)
        #
        coordinate_count = lonlat_coordinate_array.shape[0]
        band_count = geotiff_info.get("band_count")
        gcs = geotiff_info.get("gcs")
        pcs = geotiff_info.get("pcs")
        geotransform = geotiff_info.get("geotransform")
        #
        col_title = ["Coordinate_X", "Coordinate_Y"]
        for i in range(1, band_count + 1):
            col_title.append("Band_" + str(i))
        # #
        # row_title = list(range(1, coordinates_array.shape[0] + 1))
        #
        image_file_count = len(self.image_file_list)
        iterCount = image_file_count * band_count * coordinate_count
        #
        pixel_value_array = np.zeros([coordinate_count, len(col_title)], dtype = np.float64)
        pixel_value_array[:, 0:2] = lonlat_coordinate_array
        #
        for i, (img_filename, pixel_value_filename) in enumerate(zip(self.image_file_list, self.pixel_value_file_list)):
            #
            for j in range(1, band_count + 1):
                #
                img_arr = RasterImgIO.read_single_band(img_filename, j)
                tmp_pixel_value_list = []
                #
                for k, coordinates in enumerate(colrow_coordinate_array):
                    try:
                        pixel_value = PixelValueExtractor.get_value_by_coordinates(img_arr, band_count, gcs, pcs, geotransform, 
                                                                                coordinates, coordinates_type = "rowcol",
                                                                                noData = self.noData, invalidPixel=self.invalidPixel)
                    except Exception as error_Info:
                        pixel_value = np.nan
                    #
                    tmp_pixel_value_list.append(pixel_value)
                    #
                    if i == 0:
                        currentCount = (((k + 1) + (coordinate_count * (j - 1)) + i * band_count * coordinate_count))
                        statusPercent = int(round(float(currentCount / iterCount) * 100))
                    else:
                        currentCount = (((k + 1) + (coordinate_count * (j - 1)) + i * band_count * coordinate_count))
                        statusPercent = int(round(float(currentCount / iterCount) * 100))
                    if statusPercent > 99:
                        statusPercent = 99
                    #
                    self.updateFinishedStatus_signal.emit((image_file_count, i + 1, statusPercent))
                #
                pixel_value_array[:, j + 1] = tmp_pixel_value_list
            #
            ExcelIO.write_excel(pixel_value_filename, ["pixel_values",], [pixel_value_array,], row_title = None, col_title = col_title)
        #
        self.updateFinishedStatus_signal.emit((image_file_count, image_file_count, 100))




def main(setting):
    app = QApplication(sys.argv)
    pixelValueExtractorialog = PixelValueExtractorialog(setting)
    pixelValueExtractorialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

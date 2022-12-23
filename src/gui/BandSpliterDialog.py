# -*- coding: utf-8 -*-

import os
import sys

import numpy as np

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from BandSpliterDialogDesigner import Ui_BandSpliterDialog
from utils.icons import get_icon

from fileio import ModelIO, RasterImgIO
from raster import BandSplitter

class BandSpliterDialog(QDialog, Ui_BandSpliterDialog):
    '''
    '''
    img_file_list = []
    split_band_file_name = []
    band_count = 0
    valid_band = []
    split_band = []
    
    
    def __init__(self, setting):
        super(BandSpliterDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        #
        self.init_ui_element()
        self.connect_signal_slot()

    def init_ui_element(self):
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))

    def get_band_index(self, band_str):
        band_index = ""
        for char in band_str:
            if char.isdigit():
                band_index += char
        #
        return int(band_index)

    def connect_signal_slot( self ):
        self.selectFilePushButton.clicked.connect(self.selectFilePushButtonClicked)
        self.removeFilePushButton.clicked.connect(self.removeFilePushButtonClicked)
        self.clearFilePushButton.clicked.connect(self.clearFilePushButtonClicked)
        self.addSplitBandToolButton.clicked.connect(self.addSplitBandToolButtonClicked)
        self.removeSplitBandToolButton.clicked.connect(self.removeSplitBandToolButtonClicked)
        self.selectSaveStyleComboBox.currentIndexChanged.connect(self.selectSaveStyleComboBoxCurrentIndexChanged)
        self.selectSaveDirPushButton.clicked.connect(self.selectSaveDirPushButtonClicked)
        self.selectSaveFileNamePushButton.clicked.connect(self.selectSaveFileNamePushButtonClicked)
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)

    def selectFilePushButtonClicked(self):
        self.img_file_list, _ =  QFileDialog.getOpenFileNames(self, "选择一幅或多幅波段影像", os.path.expanduser('~'), "GeoTiff file(*.tif)")
        if len(self.img_file_list) >= 1:
            img_info = RasterImgIO.query_geotiff_info(self.img_file_list[0])
            self.band_count = img_info.get("band count")
        for i, file_path in enumerate(self.img_file_list):
            if i + 1 > self.fileListTableWidget.rowCount():
                self.fileListTableWidget.setRowCount(self.parameterListTableWidget.rowCount() + 5)
            for row_index in range(self.fileListTableWidget.rowCount()):
                if self.fileListTableWidget.item(row_index, 0) == None:
                    self.fileListTableWidget.setItem(row_index, 0, QTableWidgetItem(file_path))
                    tmp_name = os.path.basename(file_path)
                    out_file_name = tmp_name[:-4]+ "_Band"
                    self.split_band_file_name.append(out_file_name)
                    self.fileListTableWidget.setItem(row_index, 1, QTableWidgetItem(out_file_name))
                    break
        #
        if self.band_count > 1:
            for i in range(self.band_count):
                self.valid_band.append("Band" + str(i + 1))
        #
        self.validBandListWidget.addItems(self.valid_band)      
                   
    def removeFilePushButtonClicked(self):
        self.fileListTableWidget.removeRow(self.fileListTableWidget.currentRow())
        self.fileListTableWidget.setRowCount(self.fileListTableWidget.rowCount() + 1)

    def clearFilePushButtonClicked(self):
        self.fileListTableWidget.clearContents()

    def addSplitBandToolButtonClicked(self):
        if self.validBandListWidget.currentItem() != None:
            selectedText = self.validBandListWidget.currentItem().text()
            self.split_band.append(self.get_band_index(selectedText))
            #
            selectedIndex = self.validBandListWidget.currentRow()
            self.splitBandListWidget.addItem(self.validBandListWidget.takeItem(selectedIndex))
            self.splitBandListWidget.sortItems()

    def removeSplitBandToolButtonClicked(self):
        if self.splitBandListWidget.currentItem() != None:
            selectedText = self.splitBandListWidget.currentItem().text()
            self.split_band.remove(self.get_band_index(selectedText))
            #
            selectedIndex = self.splitBandListWidget.currentRow()
            self.validBandListWidget.insertItem(1, self.splitBandListWidget.takeItem(selectedIndex))
            self.validBandListWidget.sortItems()

    def selectSaveStyleComboBoxCurrentIndexChanged(self):
        if self.saveStyleComboBox.currentIndex() == 0:
            self.saveDirLineEdit.setEnabled(False)
            self.saveDirPushButton.setEnabled(False)
            self.saveFileNameLineEdit.setEnabled(True)
            self.saveFileNamePushButton.setEnabled(True)
        else:
            self.saveDirLineEdit.setEnabled(True)
            self.saveDirPushButton.setEnabled(True)
            self.saveFileNameLineEdit.setEnabled(False)
            self.saveFileNamePushButton.setEnabled(False)

    def selectSaveDirPushButtonClicked(self):
        file_dir =  QFileDialog.getExistingDirectory(self, "选择或新建一个保存多幅单波段影像文件的路径", os.path.expanduser('~'))
        if file_dir != "":
            self.saveDirLineEdit.setText(file_dir)

    def selectSaveFileNamePushButtonClicked(self):
        file_path, _ =  QFileDialog.getSaveFileName(self, "填写一个多波段影像文件的名字", os.path.expanduser('~'), "GeoTiff file(*.tif)")
        if file_path != "":
            self.saveFileNameLineEdit.setText(file_path)

    def okPushButtonClicked(self):
    ##        self.modelStatusGifLabel.setPixmap(QtGui.QPixmap(""))
    ##        self.modelStatusGifLabel.setMovie(self.qGif)
    ##        self.qGif.start()
    ##        self.modelStatusLabel.setText("正在拟合图像！")
        #
        if self.saveFormatComboBox.currentIndex() == 0:
            save_format = ".tif"
        else:
            save_format = ".jpg"
        #
        self.band_separation_thread = RunThread(self.img_file_list, self.split_band_file_name, self.split_band,
                                                self.saveStyleComboBox.currentText(), save_format,
                                                self.saveDirLineEdit.text(), self.saveFileNameLineEdit.text())
        self.band_separation_thread.updateFinishedStatus_signal.connect(self.updateFinishedStatus)
        self.band_separation_thread.start()  


    def updateFinishedStatus(self):
    ##        self.modelStatusGifLabel.setPixmap(self.pixmap)
    ##        self.modelStatusLabel.setText("图像拟合完成！")
        #
        if QMessageBox.information(self,"提示","已完成波段分离!", QMessageBox.Ok) == QMessageBox.Ok:
            self.close()
            

    def cancelPushButtonClicked(self):
        self.close()


class RunThread(QtCore.QThread):

   img_file_list = None
   split_band_file_name = None
   split_band = None
   save_style = None
   save_format = None
   save_dir = None
   save_file_name = None
   
   updateFinishedStatus_signal = QtCore.pyqtSignal()

   def __init__(self, img_file_list, split_band_file_name, split_band, save_style, save_format, save_dir, save_file_name):
       super().__init__()
       self.img_file_list = img_file_list
       self.split_band_file_name = split_band_file_name
       self.split_band = split_band
       self.save_style = save_style
       self.save_format = save_format
       self.save_dir = save_dir
       self.save_file_name = save_file_name

   def run(self):
       if self.save_style == "多波段文件":
           for img_file in self.img_file_list:
               BandSplitter.extract_sub_multi_band(img_file, self.split_band, self.save_format, self.save_file_name)
       else:
           for img_file, band_file_name in zip(self.img_file_list, self.split_band_file_name):
               save_file_name = os.path.join(self.save_dir, band_file_name + self.save_format)
               BandSplitter.extract_single_band(img_file, self.split_band, self.save_format, save_file_name)

       #
       self.updateFinishedStatus_signal.emit()
     
        
def main(setting):
    app = QApplication(sys.argv)
    bandSpliterDialog = BandSpliterDialog(setting)
    bandSpliterDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)


# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from InitResource import get_icon
import numpy as np

from ImageFusionSTARFMDialogDesigner import Ui_ImageFusionSTARFMDialog
from fileIO import RasterImgIO
from raster import ImageFusion

class ImageFusionSTARFMDialog(QDialog, Ui_ImageFusionSTARFMDialog):
    '''
    '''
    file_list = []
    
    def __init__( self, setting):
        super(ImageFusionSTARFMDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        #
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #
        self.connect_signal_slot()

    def connect_signal_slot( self ):
        self.openT0CoarseResolutionImagePushButton.clicked.connect(self.openT0CoarseResolutionImagePushButtonClicked)
        self.openTkCoarseResolutionImagePushButton.clicked.connect(self.openTkCoarseResolutionImagePushButtonClicked)
        self.openTkFineResolutionImagePushButton.clicked.connect(self.openTkFineResolutionImagePushButtonClicked)
        self.selectT0FineResolutionImageSaveDirPushButton.clicked.connect(self.selectT0FineResolutionImageSaveDirPushButtonClicked)
        self.okPushButton.clicked.connect(self.OkPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.CancelPushButtonClicked)

    def openT0CoarseResolutionImagePushButtonClicked(self):
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个栅格影像文件", os.path.expanduser('~'), "GeoTiff file(*.tif)")
        if file_path != "":
            self.openT0CoarseResolutionImageLineEdit.setText(file_path)

    def openTkCoarseResolutionImagePushButtonClicked(self):
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个栅格影像文件", os.path.expanduser('~'), "GeoTiff file(*.tif)")
        if file_path != "":
            self.openTkCoarseResolutionImageLineEdit.setText(file_path)

    def openTkFineResolutionImagePushButtonClicked(self):
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个栅格影像文件", os.path.expanduser('~'), "GeoTiff file(*.tif)")
        if file_path != "":
            self.openTkFineResolutionImageLineEdit.setText(file_path)

    def selectT0FineResolutionImageSaveDirPushButtonClicked(self):
        file_dir =  QFileDialog.getExistingDirectory(self, "选择或新建一个保存多幅单波段影像文件的路径", os.path.expanduser('~'))
        if file_dir != "":
            self.selectT0FineResolutionImageSaveDirLineEdit.setText(file_dir)

    def OkPushButtonClicked(self):
        #
        start_window_size = int(self.startWindowSizeLineEdit.text())
        stop_window_size = int(self.stopWindowSizeLineEdit.text())
        step_window_size = int(self.stepWindowSizeLineEdit.text())
        if start_window_size > stop_window_size:
            if QMessageBox.information(self,"提示","终止值应该大于起始值!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        if start_window_size % 2 == 0 or stop_window_size % 2 == 0:
            if QMessageBox.information(self,"提示","窗口尺寸应是奇数!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        if step_window_size % 2 != 0:
            if QMessageBox.information(self,"提示","窗口尺寸参数的遍历间隔值应是偶数!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        
        start_constant_S = float(self.startConstantSLineEdit.text())
        stop_constant_S  = float(self.stopConstantSLineEdit.text())
        step_constant_S  = float(self.stepConstantSLineEdit.text())
        if start_constant_S > stop_constant_S:
            if QMessageBox.information(self,"提示","终止值应该大于起始值!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        
        start_constant_T  = float(self.startConstantTLineEdit.text())
        stop_constant_T = float(self.stopConstantTLineEdit.text())
        step_constant_T = float(self.stepConstantTLineEdit.text())
        if start_constant_T > stop_constant_T:
            if QMessageBox.information(self,"提示","终止值应该大于起始值!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        
        start_constant_D = float(self.startConstantDLineEdit.text())
        stop_constant_D = float(self.stopConstantDLineEdit.text())
        step_constant_D = float(self.stepConstantDLineEdit.text())
        if start_constant_D > stop_constant_D:
            if QMessageBox.information(self,"提示","终止值应该大于起始值!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        
        start_constant_A =  float(self.startConstantALineEdit.text())
        stop_constant_A = float(self.stopConstantALineEdit.text())
        step_constant_A = float(self.stepConstantALineEdit.text())
        if start_constant_A > stop_constant_A:
            if QMessageBox.information(self,"提示","终止值应该大于起始值!", QMessageBox.Ok) == QMessageBox.Ok:
                return
        #
        self.statusGifLabel.setPixmap(QtGui.QPixmap(""))
        self.statusGifLabel.setMovie(self.qGif)
        self.qGif.start()
        self.statusLabel.setText("正在融合图像！")
        ##
        #
        window_size_range = np.arange(start_window_size, stop_window_size + step_window_size, step_window_size)
        constant_S_range = np.arange(start_constant_S, stop_constant_S + step_constant_S, step_constant_S)
        constant_T_range = np.arange(start_constant_T, stop_constant_T + step_constant_T, step_constant_T)
        constant_D_range = np.arange(start_constant_D, stop_constant_D + step_constant_D, step_constant_D)
        constant_A_range = np.arange(start_constant_A, stop_constant_A + step_constant_A, step_constant_A)
        #
        if window_size_range.shape[0] < 1 or  constant_S_range.shape[0] < 1 or constant_T_range.shape[0] < 1 \
           or constant_D_range.shape[0] < 1 or constant_A_range.shape[0] < 1:
            if QMessageBox.information(self,"提示","参数错误请检查!", QMessageBox.Ok) == QMessageBox.Ok:
                return         
        #
        self.image_merge_thread = RunThread(self.openT0CoarseResolutionImageLineEdit.text(),
                                            self.openTkCoarseResolutionImageLineEdit.text(),
                                            self.openTkFineResolutionImageLineEdit.text(),
                                            self.selectT0FineResolutionImageSaveDirLineEdit.text(),
                                            window_size_range,
                                            constant_S_range, constant_T_range,
                                            constant_D_range, constant_A_range)
        self.image_merge_thread.updateFinishedStatus_signal.connect(self.updateFinishedStatus)
        self.image_merge_thread.start()

    def updateFinishedStatus(self, status_info):
        if status_info == "thread_quit":
            self.statusGifLabel.setPixmap(self.pixmap)
            self.statusLabel.setText("当前图像已融合完成！")
            if QMessageBox.information(self,"提示","所有参数对应的图像已融合完成!", QMessageBox.Ok) == QMessageBox.Ok:
                self.close()
        else:
            status_info = self.statusTextEdit.append(status_info)

    def CancelPushButtonClicked(self):
        self.close()
    

class RunThread(QtCore.QThread):

    img1T0_filename = None
    img1Tk_filename = None
    img2Tk_filename = None
    save_filedir = None
    window_size_range = None
    constant_S_range = None
    constant_T_range = None
    constant_D_range = None
    constant_A_range = None
    #
    updateFinishedStatus_signal = QtCore.pyqtSignal(str)

    def __init__(self, img1T0_filename, img1Tk_filename, img2Tk_filename,
                 save_filedir, window_size_range, constant_S_range, constant_T_range, constant_D_range, constant_A_range):
        super().__init__()
        self.img1T0_filename = img1T0_filename
        self.img1Tk_filename = img1Tk_filename
        self.img2Tk_filename = img2Tk_filename
        self.save_filedir = save_filedir
        self.window_size_range = window_size_range
        self.constant_S_range = constant_S_range
        self.constant_T_range = constant_T_range
        self.constant_D_range = constant_D_range
        self.constant_A_range = constant_A_range

    def run(self):
        self.updateFinishedStatus_signal.emit("读取原始图像\n")
        img1_T0 = RasterImgIO.read_single_band(self.img1T0_filename, 1)
        img1_Tk = RasterImgIO.read_single_band(self.img1Tk_filename, 1)
        img2_Tk = RasterImgIO.read_single_band(self.img2Tk_filename, 1)
        #
        img_spatial_info = RasterImgIO.query_geotiff_info(self.img2Tk_filename)
        #
        self.updateFinishedStatus_signal.emit("正在融合图像，请稍后……\n")
        for constant_S in self.constant_S_range:
            for constant_T in self.constant_T_range:
                for constant_D in self.constant_D_range:
                    for constant_A in self.constant_A_range:
                        for window_size in self.window_size_range:
                            #
                            img2_T0 = ImageFusion.image_fusion_STARFM(img1_T0, img1_Tk, img2_Tk, window_size,
                                                                  constant_S, constant_T, constant_D, constant_A)
                            save_file_path = os.path.join(self.save_filedir, "window_size" + str(window_size) + "_" + "S" + str(constant_S) + "_" + "T" + str(constant_T) + \
                                            "_" + "D" + str(constant_D) + "_" + "A" + str(constant_A) + "_"  + ".tif")
                            RasterImgIO.write_single_band(save_file_path, img2_T0, img_spatial_info.get("crs"),img_spatial_info.get("transform"))
                            #
                            status_info1 = "已成功应用参数：\n" + "window size" + str(window_size) + "；" + "S" + str(constant_S) + "；" + "T" + str(constant_T) + \
                                            "；" + "D" + str(constant_D) + "；" + "A" + str(constant_A) + '\n'
                            status_info2 = "已成功保存图像至：" + save_file_path + '\n'
                            self.updateFinishedStatus_signal.emit(status_info1 + status_info2)
        #
        self.updateFinishedStatus_signal.emit("thread_quit")
                                

def main(setting):
    app = QApplication(sys.argv)
    imageFusionSTARFMDialog = ImageFusionSTARFMDialog(setting)
    imageFusionSTARFMDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

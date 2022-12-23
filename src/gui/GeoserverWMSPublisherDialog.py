# -*- coding: utf-8 -*-

import os
import sys

import unicodedata

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem

from GeoserverWMSPublisherDialogDesigner import Ui_GeoserverWMSPublisherDialog
from utils.icons import get_icon, get_pixmap, get_gif
from data.GeoserverManagement import GeoserverManagement

class GeoserverWMSPublisherDialog(QDialog, Ui_GeoserverWMSPublisherDialog):
    '''
    '''
    #
    qSetting = None
    model_application = []
    
    def __init__( self, setting):
        super(GeoserverWMSPublisherDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.init_ui_element()
        self.connect_signal_slot()
        #
        self.qSetting = setting
        self.geoserverManagement = None
        #

    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #
        self.selectDataFilePushButton.setIcon(get_icon("select_folder"))
        self.selectStyleFilePushButton.setIcon(get_icon("select_folder"))

    def connect_signal_slot( self ):
        #
        self.loginPushButton.clicked.connect(self.loginPushButtonClicked)
        self.isCreateNewWorkspaceCheckBox.clicked.connect(self.isCreateNewWorkspaceCheckBoxClicked)
        self.isCreateNewStyleCheckBox.clicked.connect(self.isCreateNewStyleCheckBoxClicked)
        self.selectDataFilePushButton.clicked.connect(self.selectDataFilePushButtonClicked)
        self.selectStyleFilePushButton.clicked.connect(self.selectStyleFilePushButtonClicked)
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)

    def loginPushButtonClicked(self):
        #
        curl_bin_dir = str(self.qSetting.value("curlBinDir"))
        #
        self.geoserverManagement = GeoserverManagement("localhost",
                                                       self.portLineEdit.text(),
                                                       self.usernameLineEdit.text(),
                                                       self.passwordLineEdit.text(),
                                                       curl_bin_dir)
        #
        workspaces_name = self.geoserverManagement.get_workspace_name()
        styles_name = self.geoserverManagement.get_style_name()
        #
        self.workspaceNameComboBox.addItems(workspaces_name)
        self.styleNameComboBox.addItems(styles_name)

    def isCreateNewWorkspaceCheckBoxClicked(self):
        if self.isCreateNewWorkspaceCheckBox.isChecked():
            self.newWorkspaceNameLineEdit.setEnabled(True)
            self.workspaceNameComboBox.setEnabled(False)
        else:
            self.newWorkspaceNameLineEdit.setEnabled(False)
            self.workspaceNameComboBox.setEnabled(True)

    def isCreateNewStyleCheckBoxClicked(self):
        if self.isCreateNewStyleCheckBox.isChecked():
            self.newStyleNameLineEdit.setEnabled(True)
            self.styleNameComboBox.setEnabled(False)
        else:
            self.newStyleNameLineEdit.setEnabled(False)
            self.styleNameComboBox.setEnabled(True)

    def selectDataFilePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        filepath, _ =  QFileDialog.getOpenFileName(self, "选择一个栅格影像文件",
                                                   lastFileDir,
                                                   "GeoTiff file(*.tif *.TIF)")
        self.selectDataFileLineEdit.setText(filepath)
            #
        self.qSetting.setValue("lastFileDir", os.path.dirname(filepath))

    def selectStyleFilePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        filepath, _ =  QFileDialog.getOpenFileName(self, "选择一个栅格影像文件",
                                                   lastFileDir,
                                                   "SLD file(*.sld)")
        self.selectStyleFileLineEdit.setText(filepath)
            #
        self.qSetting.setValue("lastFileDir", os.path.dirname(filepath))

    def okPushButtonClicked(self):
        #
        if self.isCreateNewWorkspaceCheckBox.isChecked():
            workspace_name = self.newWorkspaceNameLineEdit.text()
            self.geoserverManagement.create_workspace(workspace_name)
            #
            if self.isCreateNewStyleCheckBox.isChecked():
                style_filepath = self.selectStyleFileLineEdit.text()
                style_name = self.newStyleNameLineEdit.text( )
                self.geoserverManagement.create_style(style_filepath, style_name)
            else:
                style_name = self.styleNameComboBox.currentText()
        else:
            workspace_name = self.workspaceNameComboBox.currentText()
            if self.isCreateNewStyleCheckBox.isChecked():
                style_filepath = self.selectStyleFileLineEdit.text()
                style_name = self.newStyleNameLineEdit.text( )
                self.geoserverManagement.create_style(style_filepath, style_name)
            else:
                style_name = self.styleNameComboBox.currentText()
        #
        geotiff_filepath = self.selectDataFileLineEdit.text()
        layer_name = self.layerNameLineEdit.text()
        self.geoserverManagement.publish_geotiff(geotiff_filepath, workspace_name, layer_name)
        self.geoserverManagement.apply_style(style_name, workspace_name, layer_name)
        #
        QMessageBox.information(self, "提示", "WMS服务发布成功！", QMessageBox.Ok)


    def cancelPushButtonClicked(self):
        self.close()

        
def main(setting):
    app = QApplication(sys.argv)
    publishGeoserverWMSDialog = GeoserverWMSPublisherDialog(setting)
    publishGeoserverWMSDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem

from MainWindowDesigner import Ui_MainWindow
from InitResource import get_icon, get_pixmap, get_gif
from AppSettingDialog import AppSettingDialog
from SampleMakerDialog import SampleMakerDialog
from DataScalerDialog import DataScalerDialog
from FeatureCreatorDialog import FeatureCreatorDialog
from FeatureSelectorDialog import FeatureSelectorDialog
from PixelValueExtractorDialog import PixelValueExtractorialog
from BandCalculatorDialog import BandCalculatorDialog
from BandSpliterDialog import BandSpliterDialog
from ImageMergeSTARFMDialog import ImageFusionSTARFMDialog
from EmpiricalStatisticalModelDialog import EmpiricalStatisticalModelDialog
from FormulaApplicationDialog import FormulaApplicationDialog
from SelectMLTaskTypeDialog import SelectMLTaskTypeDialog
from EstimatorApplicationDialog import EstimatorApplicationDialog
from GeoserverWMSPublisherDialog import GeoserverWMSPublisherDialog
from MySQLDatabaseManagementDialog import MySQLDatabaseManagementDialog


class MainWindow(QMainWindow, Ui_MainWindow):  

    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.setupUi(self)
        #
        self.init_app_config()
        self.init_ui_element()
        self.connect_signal_slot()
    
    def init_ui_element(self):
        self.setWindowIcon(get_icon("appLogo"))

    def connect_signal_slot( self ):
        self.appSettingToolBarAction.triggered.connect(self.appSettingToolBarActionTriggered)
        self.toolBoxTreeWidget.doubleClicked.connect(self.toolBoxTreeWidgetDoubleClicked)

    def init_app_config(self):
        #
        self.setting_filename = os.path.dirname(os.path.dirname(__file__)) + \
                                                r"\resource\data\setting.ini"
        self.qSetting = QtCore.QSettings(self.setting_filename, QtCore.QSettings.IniFormat)
        #
        self.working_dir = str(self.qSetting.value("lastFileDir"))
        if self.working_dir is None or not os.path.isdir(self.working_dir):
            self.working_dir = os.path.expanduser('~')
            #
            self.qSetting.setValue("lastFileDir", self.working_dir)
        #
        self.sklearn_params_filepath = str(self.qSetting.value("sklearnParamsFilepath"))
        if self.sklearn_params_filepath is None or not os.path.isdir(self.sklearn_params_filepath):
            self.sklearn_params_filepath = os.path.dirname(os.path.dirname(__file__)) + \
                                                           r"\resource\data\sklearn_params.json"
            self.qSetting.setValue("sklearnParamsFilepath", self.sklearn_params_filepath)
        #
        self.curl_bin_dir = str(self.qSetting.value("curlBinDir"))
        if self.curl_bin_dir is None or not os.path.isdir(self.curl_bin_dir):
            self.curl_bin_dir = os.path.dirname(os.path.dirname(__file__)) + \
                                                r"\bin\curl-7.65.3-win64-mingw\bin"
            #
            self.qSetting.setValue("curlBinDir", self.curl_bin_dir)
    
    def appSettingToolBarActionTriggered(self):
        appSettingDialog = AppSettingDialog(self.qSetting)
        appSettingDialog.exec()

    def toolBoxTreeWidgetDoubleClicked(self):
        selectToolName = self.toolBoxTreeWidget.currentItem().text(0)
        #
        if selectToolName == "创建样本":
            sampleMakerDialog = SampleMakerDialog(self.qSetting)
            sampleMakerDialog.exec()
        elif selectToolName == "归一化/标准化":
            dataScalerDialog = DataScalerDialog(self.qSetting)
            dataScalerDialog.exec()
        elif selectToolName == "特征构建":
            featureCreatorDialog = FeatureCreatorDialog(self.qSetting)
            featureCreatorDialog.exec()
        elif selectToolName == "特征选择":
            featureSelectorDialog = FeatureSelectorDialog(self.qSetting)
            featureSelectorDialog.exec()
        elif selectToolName == "像元值提取":
            pixelValueExtractorialog = PixelValueExtractorialog(self.qSetting)
            pixelValueExtractorialog.exec()
        elif selectToolName == "波段计算器":
            bandCalculatorDialog = BandCalculatorDialog(self.qSetting)
            bandCalculatorDialog.exec()
        elif selectToolName == "波段分离":
            bandSpliterDialog = BandSpliterDialog(self.qSetting)
            bandSpliterDialog.exec()
        elif selectToolName == "STARFM融合":
            imageFusionSTARFMDialog = ImageFusionSTARFMDialog(self.qSetting)
            imageFusionSTARFMDialog.exec()
        elif selectToolName == "经验统计模型":
            empiricalStatisticalModelDialog = EmpiricalStatisticalModelDialog(self.qSetting)
            empiricalStatisticalModelDialog.exec()
        elif selectToolName == "应用方程":
            formulaApplicationDialog = FormulaApplicationDialog(self.qSetting)
            formulaApplicationDialog.exec()
        elif selectToolName == "scikit-learn机器学习":
            selectMLTaskTypeDialog = SelectMLTaskTypeDialog(self.qSetting)
            selectMLTaskTypeDialog.exec()
        elif selectToolName == "应用模型":
            estimatorApplicationDialog = EstimatorApplicationDialog(self.qSetting)
            estimatorApplicationDialog.exec()
        elif selectToolName == "WMS服务发布":
            geoserverWMSPublisherDialog = GeoserverWMSPublisherDialog(self.qSetting)
            geoserverWMSPublisherDialog.exec()
        elif selectToolName == "MySQL数据库管理":
            mySQLDatabaseManagementDialog = MySQLDatabaseManagementDialog(self.qSetting)
            mySQLDatabaseManagementDialog.exec()
        else:
            pass
           
    def closeEvent(self, QCloseEvent):
        qMsg = QMessageBox.question(self, "提示","退出iPyGIRS程序？")
        if qMsg == QMessageBox.Yes:
            QCloseEvent.accept()  
        else:
            QCloseEvent.ignore()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    #
    main()

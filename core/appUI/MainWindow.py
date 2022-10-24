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
from ScikitLearnMLDialog import ScikitLearnMLDialog
from EstimatorApplicationDialog import EstimatorApplicationDialog
from GeoserverWMSPublisherDialog import GeoserverWMSPublisherDialog
from MySQLDatabaseManagementDialog import MySQLDatabaseManagementDialog


class MainWindow(QMainWindow, Ui_MainWindow):  

    def __init__(self):
        super(MainWindow, self).__init__(None)
        self.setupUi(self)
        #
        self.init_app_config()
        self.init_window_ui()
        self.init_toolBar_ui()
        self.init_toolBox_ui()
        self.connect_signal_slot()
    
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

    def init_window_ui(self):
        self.setWindowIcon(get_icon("appLogo"))
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint)

    def init_toolBar_ui(self):
        self.mainToolBar = QtWidgets.QToolBar(self)
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        # 
        self.appSettingToolBarAction = QtWidgets.QAction(get_icon("toolBarAppSetting"), "设置", self)
        self.mainToolBar.addAction(self.appSettingToolBarAction)
        self.mainToolBar.addSeparator()

        self.helpToolBarAction = QtWidgets.QAction(get_icon("toolBarHelp"), "帮助", self)
        self.mainToolBar.addAction(self.helpToolBarAction)

        self.feedbackToolBarAction = QtWidgets.QAction(get_icon("toolBarFeedback"), "反馈", self)
        self.mainToolBar.addAction(self.feedbackToolBarAction)

        self.aboutToolBarAction = QtWidgets.QAction(get_icon("toolBarAbout"), "关于", self)
        self.mainToolBar.addAction(self.aboutToolBarAction)

    def init_toolBox_ui(self):
        # 数据管理
        self.toolBoxTreeWidget.topLevelItem(0).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(0).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(0).child(1).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(0).child(1).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(0).child(2).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(0).child(2).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(0).child(2).child(1).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
        # 数理统计
        self.toolBoxTreeWidget.topLevelItem(1).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(1).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(1).child(1).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
        # 地理处理
        self.toolBoxTreeWidget.topLevelItem(2).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(2).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
        # 栅格数据
        self.toolBoxTreeWidget.topLevelItem(3).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(1).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(2).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(3).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(3).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(4).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(3).child(4).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
        # 机器学习
        self.toolBoxTreeWidget.topLevelItem(4).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(4).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(4).child(1).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(4).child(2).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
        # 数据库
        self.toolBoxTreeWidget.topLevelItem(5).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(5).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
        # 地图服务
        self.toolBoxTreeWidget.topLevelItem(6).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(6).child(0).setIcon(0, get_icon("toolBoxBoxTreeWidget"))
        self.toolBoxTreeWidget.topLevelItem(6).child(0).child(0).setIcon(0, get_icon("toolBoxToolTreeWidget"))
        
    def connect_signal_slot( self ):
        self.appSettingToolBarAction.triggered.connect(self.appSettingToolBarActionTriggered)
        self.toolBoxTreeWidget.doubleClicked.connect(self.toolBoxTreeWidgetDoubleClicked)
    
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
            scikitLearnMLDialog = ScikitLearnMLDialog(self.qSetting)
            scikitLearnMLDialog.exec()
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

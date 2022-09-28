# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from InitResource import get_icon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        #
        #
        self._make_toolBar(MainWindow)
        self._make_statusBar(MainWindow)
        self._make_toolBoxWidget(MainWindow)
        #
        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _make_toolBar(self, MainWindow):
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        # 
        self.appSettingToolBarAction = QtWidgets.QAction(get_icon("appSettingToolBar"),
                                                       "系统设置", MainWindow)
        self.mainToolBar.addAction(self.appSettingToolBarAction)

        self.mainToolBar.addSeparator()
        #
        self.helpToolBarAction = QtWidgets.QAction(get_icon("helpToolBar"),
                                                   "帮助", MainWindow)
        self.mainToolBar.addAction(self.helpToolBarAction)

        self.feedbackToolBarAction = QtWidgets.QAction(get_icon("feedbackToolBar"),
                                                       "反馈", MainWindow)
        self.mainToolBar.addAction(self.feedbackToolBarAction)

        self.aboutToolBarAction = QtWidgets.QAction(get_icon("aboutToolBar"),
                                                    "关于", MainWindow)
        self.mainToolBar.addAction(self.aboutToolBarAction)

    def _make_toolBoxWidget(self, MainWindow):
        #
        self.toolBoxHorizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.toolBoxHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBoxHorizontalLayout.setSpacing(5)
        self.toolBoxHorizontalLayout.setObjectName("toolBoxHorizontalLayout")
        
        self.toolBoxTreeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.toolBoxTreeWidget.setObjectName("toolBoxTreeWidget")
        self.toolBoxTreeWidget.headerItem().setText(0, "1")
        self.toolBoxTreeWidget.setHeaderHidden(True)
        #
        self.toolBoxHorizontalLayout.addWidget(self.toolBoxTreeWidget)
        #
        ###
        dataManagementToolItem = QtWidgets.QTreeWidgetItem(self.toolBoxTreeWidget)
        dataManagementToolItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))
        sampleMakerItem = QtWidgets.QTreeWidgetItem(dataManagementToolItem)
        sampleMakerItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        ##
        preprocessorItem = QtWidgets.QTreeWidgetItem(dataManagementToolItem)
        preprocessorItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        dataScalerItem = QtWidgets.QTreeWidgetItem(preprocessorItem)
        dataScalerItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        ##
        featureProcessorItem = QtWidgets.QTreeWidgetItem(dataManagementToolItem)
        featureProcessorItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        featureCreatorItem = QtWidgets.QTreeWidgetItem(featureProcessorItem)
        featureCreatorItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        featureSelectorItem = QtWidgets.QTreeWidgetItem(featureProcessorItem)
        featureSelectorItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        ###
        rasterProcessorToolItem = QtWidgets.QTreeWidgetItem(self.toolBoxTreeWidget)
        rasterProcessorToolItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        pixelValueExtractorItem = QtWidgets.QTreeWidgetItem(rasterProcessorToolItem)
        pixelValueExtractorItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        bandCalculatorItem = QtWidgets.QTreeWidgetItem(rasterProcessorToolItem)
        bandCalculatorItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        bandSpliterItem = QtWidgets.QTreeWidgetItem(rasterProcessorToolItem)
        bandSpliterItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        baneStackerItem = QtWidgets.QTreeWidgetItem(rasterProcessorToolItem)
        baneStackerItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        imageSmoothItem = QtWidgets.QTreeWidgetItem(rasterProcessorToolItem)
        imageSmoothItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        movingAverageSmoothItem = QtWidgets.QTreeWidgetItem(imageSmoothItem)
        movingAverageSmoothItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        imageFusionItem = QtWidgets.QTreeWidgetItem(rasterProcessorToolItem)
        imageFusionItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        STARFMFusionItem = QtWidgets.QTreeWidgetItem(imageFusionItem)
        STARFMFusionItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        ###
        mathToolItem = QtWidgets.QTreeWidgetItem(self.toolBoxTreeWidget)
        mathToolItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        empiricalStatisticalModelItem = QtWidgets.QTreeWidgetItem(mathToolItem)
        empiricalStatisticalModelItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        formulaApplicationItem = QtWidgets.QTreeWidgetItem(mathToolItem)
        formulaApplicationItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        ###
        machineLearningToolItem = QtWidgets.QTreeWidgetItem(self.toolBoxTreeWidget)
        machineLearningToolItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        scikitLearnMLItem = QtWidgets.QTreeWidgetItem(machineLearningToolItem)
        scikitLearnMLItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        TPOTMLItem = QtWidgets.QTreeWidgetItem(machineLearningToolItem)
        TPOTMLItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        modelApplicationItem = QtWidgets.QTreeWidgetItem(machineLearningToolItem)
        modelApplicationItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))
        
        ###
        dataBaseToolItem = QtWidgets.QTreeWidgetItem(self.toolBoxTreeWidget)
        dataBaseToolItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        mySQLDataBaseManagementItem = QtWidgets.QTreeWidgetItem(dataBaseToolItem)
        mySQLDataBaseManagementItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

        ###
        geoserverToolItem = QtWidgets.QTreeWidgetItem(self.toolBoxTreeWidget)
        geoserverToolItem.setIcon(0, get_icon("toolBox_ToolBoxTreeWidget"))

        publishWMSItem = QtWidgets.QTreeWidgetItem(geoserverToolItem)
        publishWMSItem.setIcon(0, get_icon("tool_ToolBoxTreeWidget"))

    def _make_statusBar(self, MainWindow):
        self.mainStatusbar = QtWidgets.QStatusBar(MainWindow)
        self.mainStatusbar.setObjectName("mainStatusbar")
        MainWindow.setStatusBar(self.mainStatusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iPyGIRS V0.2.2-Beta"))
        self.mainToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

        ###
        self.toolBoxTreeWidget.setSortingEnabled(False)
        self.toolBoxTreeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "数据管理工具"))
        self.toolBoxTreeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "创建样本"))

        self.toolBoxTreeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "预处理"))
        self.toolBoxTreeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("MainWindow", "归一化/标准化"))

        self.toolBoxTreeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "特征处理"))
        self.toolBoxTreeWidget.topLevelItem(0).child(2).child(0).setText(0, _translate("MainWindow", "特征构建"))
        self.toolBoxTreeWidget.topLevelItem(0).child(2).child(1).setText(0, _translate("MainWindow", "特征选择"))

        ###
        self.toolBoxTreeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "栅格数据工具"))
        self.toolBoxTreeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "像元值提取"))
        self.toolBoxTreeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "波段计算器"))
        self.toolBoxTreeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "波段分离（不可用）"))
        self.toolBoxTreeWidget.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "波段合并（不可用）"))

        self.toolBoxTreeWidget.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "图像平滑"))
        self.toolBoxTreeWidget.topLevelItem(1).child(4).child(0).setText(0, _translate("MainWindow", "移动平均平滑（不可用）"))

        self.toolBoxTreeWidget.topLevelItem(1).child(5).setText(0, _translate("MainWindow", "图像融合"))
        self.toolBoxTreeWidget.topLevelItem(1).child(5).child(0).setText(0, _translate("MainWindow", "STARFM融合"))

        ###
        self.toolBoxTreeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "数学工具"))
        self.toolBoxTreeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "经验统计模型"))
        self.toolBoxTreeWidget.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "应用方程"))

        ###
        self.toolBoxTreeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "机器学习工具"))
        self.toolBoxTreeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "scikit-learn机器学习"))
        self.toolBoxTreeWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "TPOT机器学习（不可用）"))
        self.toolBoxTreeWidget.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "应用模型"))

        ###
        self.toolBoxTreeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "数据库工具"))
        self.toolBoxTreeWidget.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "MySQL数据库管理"))

        ###
        self.toolBoxTreeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "Geoserver工具"))
        self.toolBoxTreeWidget.topLevelItem(5).child(0).setText(0, _translate("MainWindow", "WMS服务发布"))


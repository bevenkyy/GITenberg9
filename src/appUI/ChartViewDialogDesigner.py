# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChartViewDialogDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChartViewDialog(object):
    def setupUi(self, ChartViewDialog):
        ChartViewDialog.setObjectName("ChartViewDialog")
        ChartViewDialog.resize(720, 650)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChartViewDialog)
        self.verticalLayout.setContentsMargins(2, 3, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.toolButtonHorizontalLayout.setObjectName("toolButtonHorizontalLayout")
        self.selectDataFilePushButton = QtWidgets.QPushButton(ChartViewDialog)
        self.selectDataFilePushButton.setText("")
        self.selectDataFilePushButton.setObjectName("selectDataFilePushButton")
        self.toolButtonHorizontalLayout.addWidget(self.selectDataFilePushButton)
        self.saveChartPushButton = QtWidgets.QPushButton(ChartViewDialog)
        self.saveChartPushButton.setText("")
        self.saveChartPushButton.setObjectName("saveChartPushButton")
        self.toolButtonHorizontalLayout.addWidget(self.saveChartPushButton)
        self.chartSettingPushButton = QtWidgets.QPushButton(ChartViewDialog)
        self.chartSettingPushButton.setText("")
        self.chartSettingPushButton.setObjectName("chartSettingPushButton")
        self.toolButtonHorizontalLayout.addWidget(self.chartSettingPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolButtonHorizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.toolButtonHorizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(ChartViewDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 745, 582))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.chartViewHorizontalLayout = QtWidgets.QHBoxLayout()
        self.chartViewHorizontalLayout.setObjectName("chartViewHorizontalLayout")
        self.horizontalLayout_3.addLayout(self.chartViewHorizontalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(ChartViewDialog)
        QtCore.QMetaObject.connectSlotsByName(ChartViewDialog)

    def retranslateUi(self, ChartViewDialog):
        _translate = QtCore.QCoreApplication.translate
        ChartViewDialog.setWindowTitle(_translate("ChartViewDialog", "统计图表"))


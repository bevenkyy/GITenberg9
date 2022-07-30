# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EstimatorApplicationDialogDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EstimatorApplicationDialog(object):
    def setupUi(self, EstimatorApplicationDialog):
        EstimatorApplicationDialog.setObjectName("EstimatorApplicationDialog")
        EstimatorApplicationDialog.resize(828, 527)
        self.verticalLayout = QtWidgets.QVBoxLayout(EstimatorApplicationDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileListGridLayout = QtWidgets.QGridLayout()
        self.fileListGridLayout.setContentsMargins(5, 10, 5, 10)
        self.fileListGridLayout.setSpacing(10)
        self.fileListGridLayout.setObjectName("fileListGridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fileListGridLayout.addItem(spacerItem, 0, 7, 1, 1)
        self.outputFileTypeComboBox = QtWidgets.QComboBox(EstimatorApplicationDialog)
        self.outputFileTypeComboBox.setObjectName("outputFileTypeComboBox")
        self.outputFileTypeComboBox.addItem("")
        self.outputFileTypeComboBox.addItem("")
        self.fileListGridLayout.addWidget(self.outputFileTypeComboBox, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fileListGridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fileListGridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.inputFileTypeComboBox = QtWidgets.QComboBox(EstimatorApplicationDialog)
        self.inputFileTypeComboBox.setObjectName("inputFileTypeComboBox")
        self.inputFileTypeComboBox.addItem("")
        self.inputFileTypeComboBox.addItem("")
        self.fileListGridLayout.addWidget(self.inputFileTypeComboBox, 0, 1, 1, 1)
        self.isUnifyFeaturesCheckBox = QtWidgets.QCheckBox(EstimatorApplicationDialog)
        self.isUnifyFeaturesCheckBox.setChecked(True)
        self.isUnifyFeaturesCheckBox.setObjectName("isUnifyFeaturesCheckBox")
        self.fileListGridLayout.addWidget(self.isUnifyFeaturesCheckBox, 0, 6, 1, 1)
        self.outputFileTypeLabel = QtWidgets.QLabel(EstimatorApplicationDialog)
        self.outputFileTypeLabel.setObjectName("outputFileTypeLabel")
        self.fileListGridLayout.addWidget(self.outputFileTypeLabel, 0, 3, 1, 1)
        self.inputFileTypeLabel = QtWidgets.QLabel(EstimatorApplicationDialog)
        self.inputFileTypeLabel.setObjectName("inputFileTypeLabel")
        self.fileListGridLayout.addWidget(self.inputFileTypeLabel, 0, 0, 1, 1)
        self.selectDataFilePushButton = QtWidgets.QPushButton(EstimatorApplicationDialog)
        self.selectDataFilePushButton.setText("")
        self.selectDataFilePushButton.setObjectName("selectDataFilePushButton")
        self.fileListGridLayout.addWidget(self.selectDataFilePushButton, 1, 9, 1, 1)
        self.delDataFilePushButton = QtWidgets.QPushButton(EstimatorApplicationDialog)
        self.delDataFilePushButton.setText("")
        self.delDataFilePushButton.setObjectName("delDataFilePushButton")
        self.fileListGridLayout.addWidget(self.delDataFilePushButton, 2, 9, 1, 1)
        self.clearDataFilePushButton = QtWidgets.QPushButton(EstimatorApplicationDialog)
        self.clearDataFilePushButton.setText("")
        self.clearDataFilePushButton.setObjectName("clearDataFilePushButton")
        self.fileListGridLayout.addWidget(self.clearDataFilePushButton, 3, 9, 1, 1)
        self.fileListTableWidget = QtWidgets.QTableWidget(EstimatorApplicationDialog)
        self.fileListTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fileListTableWidget.setRowCount(20)
        self.fileListTableWidget.setColumnCount(2)
        self.fileListTableWidget.setObjectName("fileListTableWidget")
        self.fileListGridLayout.addWidget(self.fileListTableWidget, 1, 0, 4, 9)
        self.verticalLayout.addLayout(self.fileListGridLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 10)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.modelFileInfoLabel = QtWidgets.QLabel(EstimatorApplicationDialog)
        self.modelFileInfoLabel.setObjectName("modelFileInfoLabel")
        self.gridLayout.addWidget(self.modelFileInfoLabel, 1, 0, 1, 1)
        self.selectModelFilePushButton = QtWidgets.QPushButton(EstimatorApplicationDialog)
        self.selectModelFilePushButton.setText("")
        self.selectModelFilePushButton.setObjectName("selectModelFilePushButton")
        self.gridLayout.addWidget(self.selectModelFilePushButton, 0, 2, 1, 1)
        self.selectModelFileLabel = QtWidgets.QLabel(EstimatorApplicationDialog)
        self.selectModelFileLabel.setObjectName("selectModelFileLabel")
        self.gridLayout.addWidget(self.selectModelFileLabel, 0, 0, 1, 1)
        self.selectModelFileLineEdit = QtWidgets.QLineEdit(EstimatorApplicationDialog)
        self.selectModelFileLineEdit.setObjectName("selectModelFileLineEdit")
        self.gridLayout.addWidget(self.selectModelFileLineEdit, 0, 1, 1, 1)
        self.modelInfoTextBrowser = QtWidgets.QTextBrowser(EstimatorApplicationDialog)
        self.modelInfoTextBrowser.setStyleSheet("background-color: rgba(240, 240, 240, 246);")
        self.modelInfoTextBrowser.setObjectName("modelInfoTextBrowser")
        self.gridLayout.addWidget(self.modelInfoTextBrowser, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 10, 5, 10)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statusLogoLabel = QtWidgets.QLabel(EstimatorApplicationDialog)
        self.statusLogoLabel.setText("")
        self.statusLogoLabel.setObjectName("statusLogoLabel")
        self.horizontalLayout.addWidget(self.statusLogoLabel)
        self.statusTipLabel = QtWidgets.QLabel(EstimatorApplicationDialog)
        self.statusTipLabel.setText("")
        self.statusTipLabel.setObjectName("statusTipLabel")
        self.horizontalLayout.addWidget(self.statusTipLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.okPushButton = QtWidgets.QPushButton(EstimatorApplicationDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(EstimatorApplicationDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(EstimatorApplicationDialog)
        QtCore.QMetaObject.connectSlotsByName(EstimatorApplicationDialog)

    def retranslateUi(self, EstimatorApplicationDialog):
        _translate = QtCore.QCoreApplication.translate
        EstimatorApplicationDialog.setWindowTitle(_translate("EstimatorApplicationDialog", "应用模型"))
        self.outputFileTypeComboBox.setItemText(0, _translate("EstimatorApplicationDialog", "GeoTiff影像"))
        self.outputFileTypeComboBox.setItemText(1, _translate("EstimatorApplicationDialog", "Excel表格数据"))
        self.inputFileTypeComboBox.setItemText(0, _translate("EstimatorApplicationDialog", "GeoTiff影像"))
        self.inputFileTypeComboBox.setItemText(1, _translate("EstimatorApplicationDialog", "Excel表格数据"))
        self.isUnifyFeaturesCheckBox.setText(_translate("EstimatorApplicationDialog", "统一特征"))
        self.outputFileTypeLabel.setText(_translate("EstimatorApplicationDialog", "输出类型："))
        self.inputFileTypeLabel.setText(_translate("EstimatorApplicationDialog", "输入类型："))
        self.modelFileInfoLabel.setText(_translate("EstimatorApplicationDialog", "模型信息："))
        self.selectModelFileLabel.setText(_translate("EstimatorApplicationDialog", "模型文件："))
        self.okPushButton.setText(_translate("EstimatorApplicationDialog", "确定"))
        self.cancelPushButton.setText(_translate("EstimatorApplicationDialog", "取消"))
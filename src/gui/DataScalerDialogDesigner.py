# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataScalerDialogDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils.icons import get_icon

class Ui_DataScalerDialog(object):
    def setupUi(self, DataScalerDialog):
        DataScalerDialog.setObjectName("DataScalerDialog")
        DataScalerDialog.resize(709, 201)
        self.verticalLayout = QtWidgets.QVBoxLayout(DataScalerDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.dataFormatLabel = QtWidgets.QLabel(DataScalerDialog)
        self.dataFormatLabel.setObjectName("dataFormatLabel")
        self.gridLayout.addWidget(self.dataFormatLabel, 0, 0, 1, 1)

        self.radioButtonGroup1 = QtWidgets.QButtonGroup(DataScalerDialog)
        self.isIncludeRowTitleCheckBox = QtWidgets.QCheckBox(DataScalerDialog)
        self.isIncludeRowTitleCheckBox.setChecked(True)
        self.isIncludeRowTitleCheckBox.setObjectName("isIncludeRowTitleCheckBox")
        self.gridLayout.addWidget(self.isIncludeRowTitleCheckBox, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.isIncludeColTitleCheckBox = QtWidgets.QCheckBox(DataScalerDialog)
        self.isIncludeColTitleCheckBox.setChecked(True)
        self.isIncludeColTitleCheckBox.setObjectName("isIncludeColTitleCheckBox")
        self.gridLayout.addWidget(self.isIncludeColTitleCheckBox, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.isRowMajorRadioButton = QtWidgets.QRadioButton(DataScalerDialog)
        self.isRowMajorRadioButton.setChecked(False)
        self.isRowMajorRadioButton.setObjectName("isRowMajorRadioButton")
        self.gridLayout.addWidget(self.isRowMajorRadioButton, 0, 5, 1, 1)
        self.radioButtonGroup1.addButton(self.isRowMajorRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.isColMajorRadioButton = QtWidgets.QRadioButton(DataScalerDialog)
        self.isColMajorRadioButton.setChecked(True)
        self.isColMajorRadioButton.setObjectName("isColMajorRadioButton")
        self.radioButtonGroup1.addButton(self.isColMajorRadioButton)
        self.gridLayout.addWidget(self.isColMajorRadioButton, 0, 7, 1, 1)

        self.selectOpenDataFileLabel = QtWidgets.QLabel(DataScalerDialog)
        self.selectOpenDataFileLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectOpenDataFileLabel.setObjectName("selectOpenDataFileLabel")
        self.gridLayout.addWidget(self.selectOpenDataFileLabel, 1, 0, 1, 1)
        self.selectOpenDataFileLineEdit = QtWidgets.QLineEdit(DataScalerDialog)
        self.selectOpenDataFileLineEdit.setObjectName("selectOpenDataFileLineEdit")
        self.gridLayout.addWidget(self.selectOpenDataFileLineEdit, 1, 1, 1, 7)
        self.selectOpenDataFilePushButton = QtWidgets.QPushButton(DataScalerDialog)
        self.selectOpenDataFilePushButton.setText("")
        self.selectOpenDataFilePushButton.setIcon(get_icon("open_file"))
        self.selectOpenDataFilePushButton.setObjectName("selectOpenDataFilePushButton")
        self.gridLayout.addWidget(self.selectOpenDataFilePushButton, 1, 8, 1, 1)

        self.radioButtonGroup2 = QtWidgets.QButtonGroup(DataScalerDialog)
        self.preprocessingAlgorithmLabel = QtWidgets.QLabel(DataScalerDialog)
        self.preprocessingAlgorithmLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.preprocessingAlgorithmLabel.setObjectName("preprocessingAlgorithmLabel")
        self.gridLayout.addWidget(self.preprocessingAlgorithmLabel, 2, 0, 1, 1)
        self.isMinMaxScalerRadioButton = QtWidgets.QRadioButton(DataScalerDialog)
        self.isMinMaxScalerRadioButton.setChecked(False)
        self.isMinMaxScalerRadioButton.setObjectName("isMinMaxScalerRadioButton")
        self.radioButtonGroup2.addButton(self.isMinMaxScalerRadioButton)
        self.gridLayout.addWidget(self.isMinMaxScalerRadioButton, 2, 1, 1, 1)
        self.isStandardScalerRadioButton = QtWidgets.QRadioButton(DataScalerDialog)
        self.isStandardScalerRadioButton.setChecked(True)
        self.isStandardScalerRadioButton.setObjectName("isStandardScalerRadioButton")
        self.radioButtonGroup2.addButton(self.isStandardScalerRadioButton)
        self.gridLayout.addWidget(self.isStandardScalerRadioButton, 2, 3, 1, 1)   
        self.minMaxScalerRangeLabel = QtWidgets.QLabel(DataScalerDialog)
        self.minMaxScalerRangeLabel.setObjectName("minMaxScalerRangeLabel")
        self.gridLayout.addWidget(self.minMaxScalerRangeLabel, 2, 5, 1, 1)
        self.minMaxScalerRangeLineEdit = QtWidgets.QLineEdit(DataScalerDialog)
        self.minMaxScalerRangeLineEdit.setEnabled(False)
        self.minMaxScalerRangeLineEdit.setObjectName("minMaxScalerRangeLineEdit")
        self.gridLayout.addWidget(self.minMaxScalerRangeLineEdit, 2, 6, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.selectSaveDataFileLabel = QtWidgets.QLabel(DataScalerDialog)
        self.selectSaveDataFileLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selectSaveDataFileLabel.setObjectName("selectSaveDataFileLabel")
        self.gridLayout.addWidget(self.selectSaveDataFileLabel, 3, 0, 1, 1)
        self.selectSaveDataFileLineEdit = QtWidgets.QLineEdit(DataScalerDialog)
        self.selectSaveDataFileLineEdit.setObjectName("selectSaveDataFileLineEdit")
        self.gridLayout.addWidget(self.selectSaveDataFileLineEdit, 3, 1, 1, 7)
        self.selectSaveDataFilePushButton = QtWidgets.QPushButton(DataScalerDialog)
        self.selectSaveDataFilePushButton.setText("")
        self.selectSaveDataFilePushButton.setIcon(get_icon("save_file"))
        self.selectSaveDataFilePushButton.setObjectName("selectSaveDataFilePushButton")
        self.gridLayout.addWidget(self.selectSaveDataFilePushButton, 3, 8, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 4, 1, 1)

        self.line = QtWidgets.QFrame(DataScalerDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 10, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.okPushButton = QtWidgets.QPushButton(DataScalerDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(DataScalerDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(DataScalerDialog)
        QtCore.QMetaObject.connectSlotsByName(DataScalerDialog)

    def retranslateUi(self, DataScalerDialog):
        _translate = QtCore.QCoreApplication.translate
        DataScalerDialog.setWindowTitle(_translate("DataScalerDialog", "归一化/标准化"))
        self.dataFormatLabel.setText(_translate("DataScalerDialog", "数据格式："))
        self.isColMajorRadioButton.setText(_translate("DataScalerDialog", "列优先"))
        self.isRowMajorRadioButton.setText(_translate("DataScalerDialog", "行优先"))
        self.isIncludeRowTitleCheckBox.setText(_translate("DataScalerDialog", "包含行标题"))
        self.isMinMaxScalerRadioButton.setText(_translate("DataScalerDialog", "归一化"))
        self.preprocessingAlgorithmLabel.setText(_translate("DataScalerDialog", "预处理方式："))
        self.selectOpenDataFileLabel.setText(_translate("DataScalerDialog", "数据文件："))
        self.isIncludeColTitleCheckBox.setText(_translate("DataScalerDialog", "包含列标题"))
        self.isStandardScalerRadioButton.setText(_translate("DataScalerDialog", "标准化"))
        self.minMaxScalerRangeLabel.setText(_translate("DataScalerDialog", "最大/小值："))
        self.minMaxScalerRangeLineEdit.setText(_translate("DataScalerDialog", "0.0~1.0"))
        self.selectSaveDataFileLabel.setText(_translate("DataScalerDialog", "保存数据："))
        self.okPushButton.setText(_translate("DataScalerDialog", "确定"))
        self.cancelPushButton.setText(_translate("DataScalerDialog", "取消"))


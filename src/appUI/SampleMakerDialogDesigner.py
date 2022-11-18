# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleMakerDialogDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2/Lib/site-packages"))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets
from InitResource import get_icon

class Ui_SampleMakerDialog(object):
    def setupUi(self, SampleMakerDialog):
        SampleMakerDialog.setObjectName("SampleMakerDialog")
        SampleMakerDialog.resize(929, 757)
        self.verticalLayout = QtWidgets.QVBoxLayout(SampleMakerDialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.parametersSettingGroupBox = QtWidgets.QGroupBox(SampleMakerDialog)
        self.parametersSettingGroupBox.setObjectName("parametersSettingGroupBox")
        self.parametersSettingGridLayout = QtWidgets.QGridLayout(self.parametersSettingGroupBox)
        self.parametersSettingGridLayout.setContentsMargins(10, -1, 10, 10)
        self.parametersSettingGridLayout.setHorizontalSpacing(5)
        self.parametersSettingGridLayout.setObjectName("parametersSettingGridLayout")
        self.selectAllSampleLineEdit = QtWidgets.QLineEdit(self.parametersSettingGroupBox)
        self.selectAllSampleLineEdit.setObjectName("selectAllSampleLineEdit")
        self.parametersSettingGridLayout.addWidget(self.selectAllSampleLineEdit, 3, 1, 1, 6)
        self.isRegressorSamplesRadioButton = QtWidgets.QRadioButton(self.parametersSettingGroupBox)
        self.isRegressorSamplesRadioButton.setChecked(True)
        self.isRegressorSamplesRadioButton.setObjectName("isRegressorSamplesRadioButton")
        self.parametersSettingGridLayout.addWidget(self.isRegressorSamplesRadioButton, 0, 3, 1, 1)
        self.isClassifierSamplesRadioButton = QtWidgets.QRadioButton(self.parametersSettingGroupBox)
        self.isClassifierSamplesRadioButton.setObjectName("isClassifierSamplesRadioButton")
        self.parametersSettingGridLayout.addWidget(self.isClassifierSamplesRadioButton, 0, 4, 1, 1)
        self.isIncludeRowTitleCheckBox = QtWidgets.QCheckBox(self.parametersSettingGroupBox)
        self.isIncludeRowTitleCheckBox.setChecked(True)
        self.isIncludeRowTitleCheckBox.setObjectName("isIncludeRowTitleCheckBox")
        self.parametersSettingGridLayout.addWidget(self.isIncludeRowTitleCheckBox, 0, 1, 1, 1)
        self.isIncludeColTitleCheckBox = QtWidgets.QCheckBox(self.parametersSettingGroupBox)
        self.isIncludeColTitleCheckBox.setChecked(True)
        self.isIncludeColTitleCheckBox.setObjectName("isIncludeColTitleCheckBox")
        self.parametersSettingGridLayout.addWidget(self.isIncludeColTitleCheckBox, 0, 2, 1, 1)
        self.testSampleSizeDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.parametersSettingGroupBox)
        self.testSampleSizeDoubleSpinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.testSampleSizeDoubleSpinBox.setProperty("value", 0.3)
        self.testSampleSizeDoubleSpinBox.setProperty("singleStep",0.01)
        self.testSampleSizeDoubleSpinBox.setObjectName("testSampleSizeDoubleSpinBox")
        self.parametersSettingGridLayout.addWidget(self.testSampleSizeDoubleSpinBox, 0, 6, 1, 1)
        self.testSampleSizeLabel = QtWidgets.QLabel(self.parametersSettingGroupBox)
        self.testSampleSizeLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.testSampleSizeLabel.setObjectName("testSampleSizeLabel")
        self.parametersSettingGridLayout.addWidget(self.testSampleSizeLabel, 0, 5, 1, 1)
        self.selectAllSampleLabel = QtWidgets.QLabel(self.parametersSettingGroupBox)
        self.selectAllSampleLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.selectAllSampleLabel.setObjectName("selectAllSampleLabel")
        self.parametersSettingGridLayout.addWidget(self.selectAllSampleLabel, 3, 0, 1, 1)
        self.selectAllSamplePushButton = QtWidgets.QPushButton(self.parametersSettingGroupBox)
        self.selectAllSamplePushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.selectAllSamplePushButton.setText("")
        self.selectAllSamplePushButton.setIcon(get_icon("open_file"))
        self.selectAllSamplePushButton.setObjectName("selectAllSamplePushButton")
        self.parametersSettingGridLayout.addWidget(self.selectAllSamplePushButton, 3, 7, 1, 1)
        self.verticalLayout.addWidget(self.parametersSettingGroupBox)
        self.sampleDistributionGroupBox = QtWidgets.QGroupBox(SampleMakerDialog)
        self.sampleDistributionGroupBox.setObjectName("sampleDistributionGroupBox")
        self.sampleDistributionHorizontalLayout = QtWidgets.QHBoxLayout(self.sampleDistributionGroupBox)
        self.sampleDistributionHorizontalLayout.setContentsMargins(0, 5, 0, 5)
        self.sampleDistributionHorizontalLayout.setSpacing(5)
        self.sampleDistributionHorizontalLayout.setObjectName("sampleDistributionHorizontalLayout")
        self.sampleDistributionChartGridLayout = QtWidgets.QGridLayout()
        self.sampleDistributionChartGridLayout.setObjectName("sampleDistributionChartGridLayout")
        self.sampleDistributionHorizontalLayout.addLayout(self.sampleDistributionChartGridLayout)
        self.verticalLayout.addWidget(self.sampleDistributionGroupBox)
        self.outputGroupBox = QtWidgets.QGroupBox(SampleMakerDialog)
        self.outputGroupBox.setObjectName("outputGroupBox")
        self.outputGridLayout = QtWidgets.QGridLayout(self.outputGroupBox)
        self.outputGridLayout.setObjectName("outputGridLayout")
        self.saveTrainingCVSamplePushButton = QtWidgets.QPushButton(self.outputGroupBox)
        self.saveTrainingCVSamplePushButton.setText("")
        self.saveTrainingCVSamplePushButton.setIcon(get_icon("save_file"))
        self.saveTrainingCVSamplePushButton.setObjectName("saveTrainingCVSamplePushButton")
        self.outputGridLayout.addWidget(self.saveTrainingCVSamplePushButton, 0, 2, 1, 1)
        self.saveTestSampleLineEdit = QtWidgets.QLineEdit(self.outputGroupBox)
        self.saveTestSampleLineEdit.setObjectName("saveTestSampleLineEdit")
        self.outputGridLayout.addWidget(self.saveTestSampleLineEdit, 1, 1, 1, 1)
        self.saveTestSamplePushButton = QtWidgets.QPushButton(self.outputGroupBox)
        self.saveTestSamplePushButton.setText("")
        self.saveTestSamplePushButton.setIcon(get_icon("save_file"))
        self.saveTestSamplePushButton.setObjectName("saveTestSamplePushButton")
        self.outputGridLayout.addWidget(self.saveTestSamplePushButton, 1, 2, 1, 1)
        self.saveSampleDistributionChartLineEdit = QtWidgets.QLineEdit(self.outputGroupBox)
        self.saveSampleDistributionChartLineEdit.setEnabled(False)
        self.saveSampleDistributionChartLineEdit.setObjectName("saveSampleDistributionChartLineEdit")
        self.outputGridLayout.addWidget(self.saveSampleDistributionChartLineEdit, 2, 1, 1, 1)
        self.saveSampleDistributionChartPushButton = QtWidgets.QPushButton(self.outputGroupBox)
        self.saveSampleDistributionChartPushButton.setEnabled(False)
        self.saveSampleDistributionChartPushButton.setText("")
        self.saveSampleDistributionChartPushButton.setIcon(get_icon("save_file"))
        self.saveSampleDistributionChartPushButton.setObjectName("saveSampleDistributionChartPushButton")
        self.outputGridLayout.addWidget(self.saveSampleDistributionChartPushButton, 2, 2, 1, 1)
        self.saveTrainingCVSampleLineEdit = QtWidgets.QLineEdit(self.outputGroupBox)
        self.saveTrainingCVSampleLineEdit.setObjectName("saveTrainingCVSampleLineEdit")
        self.outputGridLayout.addWidget(self.saveTrainingCVSampleLineEdit, 0, 1, 1, 1)
        self.saveTrainingCVSampleLabel = QtWidgets.QLabel(self.outputGroupBox)
        self.saveTrainingCVSampleLabel.setObjectName("saveTrainingCVSampleLabel")
        self.outputGridLayout.addWidget(self.saveTrainingCVSampleLabel, 0, 0, 1, 1)
        self.saveTestSampleLabel = QtWidgets.QLabel(self.outputGroupBox)
        self.saveTestSampleLabel.setObjectName("saveTestSampleLabel")
        self.outputGridLayout.addWidget(self.saveTestSampleLabel, 1, 0, 1, 1)
        self.saveSampleDistributionChartLabel = QtWidgets.QLabel(self.outputGroupBox)
        self.saveSampleDistributionChartLabel.setObjectName("saveSampleDistributionChartLabel")
        self.outputGridLayout.addWidget(self.saveSampleDistributionChartLabel, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.outputGroupBox)
        self.okCancelButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.okCancelButtonHorizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.okCancelButtonHorizontalLayout.setSpacing(5)
        self.okCancelButtonHorizontalLayout.setObjectName("okCancelButtonHorizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.okCancelButtonHorizontalLayout.addItem(spacerItem)
        self.okPushButton = QtWidgets.QPushButton(SampleMakerDialog)
        self.okPushButton.setObjectName("okPushButton")
        self.okCancelButtonHorizontalLayout.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(SampleMakerDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.okCancelButtonHorizontalLayout.addWidget(self.cancelPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.okCancelButtonHorizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.okCancelButtonHorizontalLayout)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(SampleMakerDialog)
        QtCore.QMetaObject.connectSlotsByName(SampleMakerDialog)

    def retranslateUi(self, SampleMakerDialog):
        _translate = QtCore.QCoreApplication.translate
        SampleMakerDialog.setWindowTitle(_translate("SampleMakerDialog", "创建样本"))
        self.parametersSettingGroupBox.setTitle(_translate("SampleMakerDialog", "参数设置"))
        self.isRegressorSamplesRadioButton.setText(_translate("SampleMakerDialog", "回归样本"))
        self.isClassifierSamplesRadioButton.setText(_translate("SampleMakerDialog", "分类样本"))
        self.isIncludeRowTitleCheckBox.setText(_translate("SampleMakerDialog", "包含行标题"))
        self.isIncludeColTitleCheckBox.setText(_translate("SampleMakerDialog", "包含列标题"))
        self.testSampleSizeLabel.setText(_translate("SampleMakerDialog", "测试样本比例："))
        self.selectAllSampleLabel.setText(_translate("SampleMakerDialog", "总体样本："))
        self.sampleDistributionGroupBox.setTitle(_translate("SampleMakerDialog", "样本分布图表"))
        self.outputGroupBox.setTitle(_translate("SampleMakerDialog", "输出"))
        self.saveTrainingCVSampleLabel.setText(_translate("SampleMakerDialog", "训练验证样本："))
        self.saveTestSampleLabel.setText(_translate("SampleMakerDialog", "测试样本："))
        self.saveSampleDistributionChartLabel.setText(_translate("SampleMakerDialog", "样本分布图表："))
        self.okPushButton.setText(_translate("SampleMakerDialog", "确定"))
        self.cancelPushButton.setText(_translate("SampleMakerDialog", "取消"))

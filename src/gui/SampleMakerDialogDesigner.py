# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SampleMakerDialogDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SampleMakerDialog(object):
    def setupUi(self, SampleMakerDialog):
        SampleMakerDialog.setObjectName("SampleMakerDialog")
        SampleMakerDialog.resize(1006, 619)
        SampleMakerDialog.setStyleSheet("")
        self.topDialogVerticalLayout = QtWidgets.QVBoxLayout(SampleMakerDialog)
        self.topDialogVerticalLayout.setContentsMargins(5, 10, 5, 10)
        self.topDialogVerticalLayout.setSpacing(5)
        self.topDialogVerticalLayout.setObjectName("topDialogVerticalLayout")
        self.topOperationWidgetGridLayout = QtWidgets.QGridLayout()
        self.topOperationWidgetGridLayout.setContentsMargins(-1, -1, -1, 10)
        self.topOperationWidgetGridLayout.setObjectName("topOperationWidgetGridLayout")
        self.operationTitleLabel = QtWidgets.QLabel(SampleMakerDialog)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.operationTitleLabel.setFont(font)
        self.operationTitleLabel.setObjectName("operationTitleLabel")
        self.topOperationWidgetGridLayout.addWidget(self.operationTitleLabel, 0, 1, 1, 1)
        self.operationDescriptionLabel = QtWidgets.QLabel(SampleMakerDialog)
        self.operationDescriptionLabel.setObjectName("operationDescriptionLabel")
        self.topOperationWidgetGridLayout.addWidget(self.operationDescriptionLabel, 1, 1, 1, 1)
        self.operationLogoLabel = QtWidgets.QLabel(SampleMakerDialog)
        self.operationLogoLabel.setObjectName("operationLogoLabel")
        self.topOperationWidgetGridLayout.addWidget(self.operationLogoLabel, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topOperationWidgetGridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.topDialogVerticalLayout.addLayout(self.topOperationWidgetGridLayout)
        self.sampleMakerStackedWidget = QtWidgets.QStackedWidget(SampleMakerDialog)
        self.sampleMakerStackedWidget.setObjectName("sampleMakerStackedWidget")
        self.selectAllSamplePage = QtWidgets.QWidget()
        self.selectAllSamplePage.setObjectName("selectAllSamplePage")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.selectAllSamplePage)
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selectAllSamplePageVerticalLayout = QtWidgets.QVBoxLayout()
        self.selectAllSamplePageVerticalLayout.setObjectName("selectAllSamplePageVerticalLayout")
        self.sampleSettingGroupBox = QtWidgets.QGroupBox(self.selectAllSamplePage)
        self.sampleSettingGroupBox.setObjectName("sampleSettingGroupBox")
        self.sampleSettingGroupBoxGridLayout = QtWidgets.QGridLayout(self.sampleSettingGroupBox)
        self.sampleSettingGroupBoxGridLayout.setContentsMargins(5, 10, 5, 10)
        self.sampleSettingGroupBoxGridLayout.setVerticalSpacing(15)
        self.sampleSettingGroupBoxGridLayout.setObjectName("sampleSettingGroupBoxGridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sampleSettingGroupBoxGridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.isIncludeRowTitleCheckBox = QtWidgets.QCheckBox(self.sampleSettingGroupBox)
        self.isIncludeRowTitleCheckBox.setChecked(True)
        self.isIncludeRowTitleCheckBox.setObjectName("isIncludeRowTitleCheckBox")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.isIncludeRowTitleCheckBox, 1, 1, 1, 1)
        self.selectAllSampleLineEdit = QtWidgets.QLineEdit(self.sampleSettingGroupBox)
        self.selectAllSampleLineEdit.setObjectName("selectAllSampleLineEdit")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.selectAllSampleLineEdit, 4, 1, 1, 9)
        self.isIncludeColTitleCheckBox = QtWidgets.QCheckBox(self.sampleSettingGroupBox)
        self.isIncludeColTitleCheckBox.setChecked(True)
        self.isIncludeColTitleCheckBox.setObjectName("isIncludeColTitleCheckBox")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.isIncludeColTitleCheckBox, 1, 3, 1, 1)
        self.sampleTypeLabel = QtWidgets.QLabel(self.sampleSettingGroupBox)
        self.sampleTypeLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sampleTypeLabel.setObjectName("sampleTypeLabel")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.sampleTypeLabel, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sampleSettingGroupBoxGridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.isColMajorRadioButton = QtWidgets.QRadioButton(self.sampleSettingGroupBox)
        self.isColMajorRadioButton.setObjectName("isColMajorRadioButton")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.isColMajorRadioButton, 1, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sampleSettingGroupBoxGridLayout.addItem(spacerItem3, 1, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sampleSettingGroupBoxGridLayout.addItem(spacerItem4, 1, 6, 1, 1)
        self.selectAllSampleLabel = QtWidgets.QLabel(self.sampleSettingGroupBox)
        self.selectAllSampleLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        self.selectAllSampleLabel.setObjectName("selectAllSampleLabel")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.selectAllSampleLabel, 4, 0, 1, 1)
        self.isRowMajorRadioButton = QtWidgets.QRadioButton(self.sampleSettingGroupBox)
        self.isRowMajorRadioButton.setChecked(True)
        self.isRowMajorRadioButton.setObjectName("isRowMajorRadioButton")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.isRowMajorRadioButton, 1, 5, 1, 1)
        self.selectAllSamplePushButton = QtWidgets.QPushButton(self.sampleSettingGroupBox)
        self.selectAllSamplePushButton.setText("")
        self.selectAllSamplePushButton.setObjectName("selectAllSamplePushButton")
        self.sampleSettingGroupBoxGridLayout.addWidget(self.selectAllSamplePushButton, 4, 10, 1, 1)
        self.selectAllSamplePageVerticalLayout.addWidget(self.sampleSettingGroupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.allSampleDistributionFrame = QtWidgets.QFrame(self.selectAllSamplePage)
        self.allSampleDistributionFrame.setStyleSheet("background-color:white")
        self.allSampleDistributionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allSampleDistributionFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.allSampleDistributionFrame.setObjectName("allSampleDistributionFrame")
        self.horizontalLayout.addWidget(self.allSampleDistributionFrame)
        self.allSampleInfoGroupBox = QtWidgets.QGroupBox(self.selectAllSamplePage)
        self.allSampleInfoGroupBox.setTitle("")
        self.allSampleInfoGroupBox.setObjectName("allSampleInfoGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.allSampleInfoGroupBox)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.countNanTipLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.countNanTipLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.countNanTipLabel.setObjectName("countNanTipLabel")
        self.gridLayout_2.addWidget(self.countNanTipLabel, 3, 0, 1, 1)
        self.allSampleTypeComboBox = QtWidgets.QComboBox(self.allSampleInfoGroupBox)
        self.allSampleTypeComboBox.setObjectName("allSampleTypeComboBox")
        self.allSampleTypeComboBox.addItem("")
        self.allSampleTypeComboBox.addItem("")
        self.gridLayout_2.addWidget(self.allSampleTypeComboBox, 0, 1, 1, 1)
        self.countAllSamplesLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.countAllSamplesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countAllSamplesLabel.setObjectName("countAllSamplesLabel")
        self.gridLayout_2.addWidget(self.countAllSamplesLabel, 1, 1, 1, 1)
        self.countNanLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.countNanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countNanLabel.setObjectName("countNanLabel")
        self.gridLayout_2.addWidget(self.countNanLabel, 3, 1, 1, 1)
        self.countFeaturesTipLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.countFeaturesTipLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.countFeaturesTipLabel.setObjectName("countFeaturesTipLabel")
        self.gridLayout_2.addWidget(self.countFeaturesTipLabel, 2, 0, 1, 1)
        self.countAllSamplesTipLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.countAllSamplesTipLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.countAllSamplesTipLabel.setObjectName("countAllSamplesTipLabel")
        self.gridLayout_2.addWidget(self.countAllSamplesTipLabel, 1, 0, 1, 1)
        self.countFeaturesLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.countFeaturesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.countFeaturesLabel.setObjectName("countFeaturesLabel")
        self.gridLayout_2.addWidget(self.countFeaturesLabel, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 4, 0, 1, 1)
        self.allSampleTypeLabel = QtWidgets.QLabel(self.allSampleInfoGroupBox)
        self.allSampleTypeLabel.setObjectName("allSampleTypeLabel")
        self.gridLayout_2.addWidget(self.allSampleTypeLabel, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.allSampleInfoGroupBox)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.selectAllSamplePageVerticalLayout.addLayout(self.horizontalLayout)
        self.selectAllSamplePageVerticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.selectAllSamplePageVerticalLayout)
        self.sampleMakerStackedWidget.addWidget(self.selectAllSamplePage)
        self.setParameterPage = QtWidgets.QWidget()
        self.setParameterPage.setObjectName("setParameterPage")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.setParameterPage)
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scikitLearnSettingGroupBox = QtWidgets.QGroupBox(self.setParameterPage)
        self.scikitLearnSettingGroupBox.setObjectName("scikitLearnSettingGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scikitLearnSettingGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 6, 1, 1)
        self.shuffleSampleCheckBox = QtWidgets.QCheckBox(self.scikitLearnSettingGroupBox)
        self.shuffleSampleCheckBox.setChecked(True)
        self.shuffleSampleCheckBox.setObjectName("shuffleSampleCheckBox")
        self.gridLayout_5.addWidget(self.shuffleSampleCheckBox, 0, 0, 1, 1)
        self.sampleAlgorithmLabel = QtWidgets.QLabel(self.scikitLearnSettingGroupBox)
        self.sampleAlgorithmLabel.setObjectName("sampleAlgorithmLabel")
        self.gridLayout_5.addWidget(self.sampleAlgorithmLabel, 0, 3, 1, 1)
        self.testSampleSizeDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.scikitLearnSettingGroupBox)
        self.testSampleSizeDoubleSpinBox.setMinimum(0.0)
        self.testSampleSizeDoubleSpinBox.setSingleStep(0.05)
        self.testSampleSizeDoubleSpinBox.setProperty("value", 0.3)
        self.testSampleSizeDoubleSpinBox.setObjectName("testSampleSizeDoubleSpinBox")
        self.gridLayout_5.addWidget(self.testSampleSizeDoubleSpinBox, 0, 12, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 0, 10, 1, 1)
        self.testSampleSizeLabel = QtWidgets.QLabel(self.scikitLearnSettingGroupBox)
        self.testSampleSizeLabel.setObjectName("testSampleSizeLabel")
        self.gridLayout_5.addWidget(self.testSampleSizeLabel, 0, 11, 1, 1)
        self.preprocessingAlgorithmlabel = QtWidgets.QLabel(self.scikitLearnSettingGroupBox)
        self.preprocessingAlgorithmlabel.setObjectName("preprocessingAlgorithmlabel")
        self.gridLayout_5.addWidget(self.preprocessingAlgorithmlabel, 0, 7, 1, 1)
        self.sampleAlgorithmComboBox = QtWidgets.QComboBox(self.scikitLearnSettingGroupBox)
        self.sampleAlgorithmComboBox.setObjectName("sampleAlgorithmComboBox")
        self.sampleAlgorithmComboBox.addItem("")
        self.sampleAlgorithmComboBox.addItem("")
        self.gridLayout_5.addWidget(self.sampleAlgorithmComboBox, 0, 4, 1, 1)
        self.preprocessingAlgorithmComboBox = QtWidgets.QComboBox(self.scikitLearnSettingGroupBox)
        self.preprocessingAlgorithmComboBox.setObjectName("preprocessingAlgorithmComboBox")
        self.preprocessingAlgorithmComboBox.addItem("")
        self.preprocessingAlgorithmComboBox.addItem("")
        self.gridLayout_5.addWidget(self.preprocessingAlgorithmComboBox, 0, 8, 1, 1)
        self.horizontalLayout_4.addWidget(self.scikitLearnSettingGroupBox)
        self.makeSamplePushButton = QtWidgets.QPushButton(self.setParameterPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.makeSamplePushButton.sizePolicy().hasHeightForWidth())
        self.makeSamplePushButton.setSizePolicy(sizePolicy)
        self.makeSamplePushButton.setObjectName("makeSamplePushButton")
        self.horizontalLayout_4.addWidget(self.makeSamplePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.sampleDistributionGroupBox = QtWidgets.QGroupBox(self.setParameterPage)
        self.sampleDistributionGroupBox.setObjectName("sampleDistributionGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sampleDistributionGroupBox)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.trainingCvTestSampleDistributionFrame = QtWidgets.QFrame(self.sampleDistributionGroupBox)
        self.trainingCvTestSampleDistributionFrame.setStyleSheet("background-color:white")
        self.trainingCvTestSampleDistributionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trainingCvTestSampleDistributionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trainingCvTestSampleDistributionFrame.setObjectName("trainingCvTestSampleDistributionFrame")
        self.horizontalLayout_3.addWidget(self.trainingCvTestSampleDistributionFrame)
        self.verticalLayout.addWidget(self.sampleDistributionGroupBox)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.sampleMakerStackedWidget.addWidget(self.setParameterPage)
        self.saveEstimatorDataPage = QtWidgets.QWidget()
        self.saveEstimatorDataPage.setObjectName("saveEstimatorDataPage")
        self.saveModelHorizontalLayout = QtWidgets.QHBoxLayout(self.saveEstimatorDataPage)
        self.saveModelHorizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.saveModelHorizontalLayout.setSpacing(5)
        self.saveModelHorizontalLayout.setObjectName("saveModelHorizontalLayout")
        self.saveSampleGroupBox = QtWidgets.QGroupBox(self.saveEstimatorDataPage)
        self.saveSampleGroupBox.setObjectName("saveSampleGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.saveSampleGroupBox)
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.saveTrainingCVSampleLabel = QtWidgets.QLabel(self.saveSampleGroupBox)
        self.saveTrainingCVSampleLabel.setObjectName("saveTrainingCVSampleLabel")
        self.gridLayout.addWidget(self.saveTrainingCVSampleLabel, 0, 0, 1, 1)
        self.saveTrainingCVSampleLineEdit = QtWidgets.QLineEdit(self.saveSampleGroupBox)
        self.saveTrainingCVSampleLineEdit.setObjectName("saveTrainingCVSampleLineEdit")
        self.gridLayout.addWidget(self.saveTrainingCVSampleLineEdit, 0, 1, 1, 1)
        self.saveTrainingCVSamplePushButton = QtWidgets.QPushButton(self.saveSampleGroupBox)
        self.saveTrainingCVSamplePushButton.setText("")
        self.saveTrainingCVSamplePushButton.setObjectName("saveTrainingCVSamplePushButton")
        self.gridLayout.addWidget(self.saveTrainingCVSamplePushButton, 0, 2, 1, 1)
        self.saveTestSampleLabel = QtWidgets.QLabel(self.saveSampleGroupBox)
        self.saveTestSampleLabel.setObjectName("saveTestSampleLabel")
        self.gridLayout.addWidget(self.saveTestSampleLabel, 1, 0, 1, 1)
        self.saveTestSampleLineEdit = QtWidgets.QLineEdit(self.saveSampleGroupBox)
        self.saveTestSampleLineEdit.setObjectName("saveTestSampleLineEdit")
        self.gridLayout.addWidget(self.saveTestSampleLineEdit, 1, 1, 1, 1)
        self.saveTestSamplePushButton = QtWidgets.QPushButton(self.saveSampleGroupBox)
        self.saveTestSamplePushButton.setText("")
        self.saveTestSamplePushButton.setObjectName("saveTestSamplePushButton")
        self.gridLayout.addWidget(self.saveTestSamplePushButton, 1, 2, 1, 1)
        self.saveSampleDistributionChartLabel = QtWidgets.QLabel(self.saveSampleGroupBox)
        self.saveSampleDistributionChartLabel.setObjectName("saveSampleDistributionChartLabel")
        self.gridLayout.addWidget(self.saveSampleDistributionChartLabel, 2, 0, 1, 1)
        self.saveSampleDistributionChartLineEdit = QtWidgets.QLineEdit(self.saveSampleGroupBox)
        self.saveSampleDistributionChartLineEdit.setObjectName("saveSampleDistributionChartLineEdit")
        self.gridLayout.addWidget(self.saveSampleDistributionChartLineEdit, 2, 1, 1, 1)
        self.saveSampleDistributionChartPushButton = QtWidgets.QPushButton(self.saveSampleGroupBox)
        self.saveSampleDistributionChartPushButton.setText("")
        self.saveSampleDistributionChartPushButton.setObjectName("saveSampleDistributionChartPushButton")
        self.gridLayout.addWidget(self.saveSampleDistributionChartPushButton, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.saveSamplesResultPushButton = QtWidgets.QPushButton(self.saveSampleGroupBox)
        self.saveSamplesResultPushButton.setObjectName("saveSamplesResultPushButton")
        self.horizontalLayout_5.addWidget(self.saveSamplesResultPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 301, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.saveModelHorizontalLayout.addWidget(self.saveSampleGroupBox)
        self.sampleMakerStackedWidget.addWidget(self.saveEstimatorDataPage)
        self.topDialogVerticalLayout.addWidget(self.sampleMakerStackedWidget)
        self.bottomOperationWidgetHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomOperationWidgetHorizontalLayout.setContentsMargins(-1, 5, -1, -1)
        self.bottomOperationWidgetHorizontalLayout.setObjectName("bottomOperationWidgetHorizontalLayout")
        self.stepLogoLabel = QtWidgets.QLabel(SampleMakerDialog)
        self.stepLogoLabel.setObjectName("stepLogoLabel")
        self.bottomOperationWidgetHorizontalLayout.addWidget(self.stepLogoLabel)
        self.stepTipLabel = QtWidgets.QLabel(SampleMakerDialog)
        self.stepTipLabel.setObjectName("stepTipLabel")
        self.bottomOperationWidgetHorizontalLayout.addWidget(self.stepTipLabel)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomOperationWidgetHorizontalLayout.addItem(spacerItem11)
        self.previousStepPushButton = QtWidgets.QPushButton(SampleMakerDialog)
        self.previousStepPushButton.setEnabled(False)
        self.previousStepPushButton.setObjectName("previousStepPushButton")
        self.bottomOperationWidgetHorizontalLayout.addWidget(self.previousStepPushButton)
        self.nextStepPushButton = QtWidgets.QPushButton(SampleMakerDialog)
        self.nextStepPushButton.setObjectName("nextStepPushButton")
        self.bottomOperationWidgetHorizontalLayout.addWidget(self.nextStepPushButton)
        self.cancelFinishPushButton = QtWidgets.QPushButton(SampleMakerDialog)
        self.cancelFinishPushButton.setObjectName("cancelFinishPushButton")
        self.bottomOperationWidgetHorizontalLayout.addWidget(self.cancelFinishPushButton)
        self.topDialogVerticalLayout.addLayout(self.bottomOperationWidgetHorizontalLayout)

        self.retranslateUi(SampleMakerDialog)
        self.sampleMakerStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SampleMakerDialog)

    def retranslateUi(self, SampleMakerDialog):
        _translate = QtCore.QCoreApplication.translate
        SampleMakerDialog.setWindowTitle(_translate("SampleMakerDialog", "创建样本"))
        self.operationTitleLabel.setText(_translate("SampleMakerDialog", "保存样本"))
        self.operationDescriptionLabel.setText(_translate("SampleMakerDialog", "选择用以划分训练、验证和测试的总体样本数据源"))
        self.operationLogoLabel.setText(_translate("SampleMakerDialog", "TextLabel"))
        self.sampleSettingGroupBox.setTitle(_translate("SampleMakerDialog", "样本设置"))
        self.isIncludeRowTitleCheckBox.setText(_translate("SampleMakerDialog", "包含行标题"))
        self.isIncludeColTitleCheckBox.setText(_translate("SampleMakerDialog", "包含列标题"))
        self.sampleTypeLabel.setText(_translate("SampleMakerDialog", "样本文件类型："))
        self.isColMajorRadioButton.setText(_translate("SampleMakerDialog", "列优先"))
        self.selectAllSampleLabel.setText(_translate("SampleMakerDialog", "总体样本："))
        self.isRowMajorRadioButton.setText(_translate("SampleMakerDialog", "行优先"))
        self.countNanTipLabel.setText(_translate("SampleMakerDialog", "Nan数："))
        self.allSampleTypeComboBox.setItemText(0, _translate("SampleMakerDialog", "分类样本"))
        self.allSampleTypeComboBox.setItemText(1, _translate("SampleMakerDialog", "回归样本"))
        self.countAllSamplesLabel.setText(_translate("SampleMakerDialog", "-"))
        self.countNanLabel.setText(_translate("SampleMakerDialog", "-"))
        self.countFeaturesTipLabel.setText(_translate("SampleMakerDialog", "特征数："))
        self.countAllSamplesTipLabel.setText(_translate("SampleMakerDialog", "样本数："))
        self.countFeaturesLabel.setText(_translate("SampleMakerDialog", "-"))
        self.allSampleTypeLabel.setText(_translate("SampleMakerDialog", "样本类型："))
        self.scikitLearnSettingGroupBox.setTitle(_translate("SampleMakerDialog", "参数设置"))
        self.shuffleSampleCheckBox.setText(_translate("SampleMakerDialog", "打乱样本"))
        self.sampleAlgorithmLabel.setText(_translate("SampleMakerDialog", "抽样方法："))
        self.testSampleSizeLabel.setText(_translate("SampleMakerDialog", "测试样本比列："))
        self.preprocessingAlgorithmlabel.setText(_translate("SampleMakerDialog", "预处理："))
        self.sampleAlgorithmComboBox.setItemText(0, _translate("SampleMakerDialog", "分层抽样"))
        self.sampleAlgorithmComboBox.setItemText(1, _translate("SampleMakerDialog", "随机抽样"))
        self.preprocessingAlgorithmComboBox.setItemText(0, _translate("SampleMakerDialog", "归一化"))
        self.preprocessingAlgorithmComboBox.setItemText(1, _translate("SampleMakerDialog", "标准化"))
        self.makeSamplePushButton.setText(_translate("SampleMakerDialog", "创建"))
        self.sampleDistributionGroupBox.setTitle(_translate("SampleMakerDialog", "样本分布图表"))
        self.saveSampleGroupBox.setTitle(_translate("SampleMakerDialog", "保存设置"))
        self.saveTrainingCVSampleLabel.setText(_translate("SampleMakerDialog", "训练-验证样本："))
        self.saveTestSampleLabel.setText(_translate("SampleMakerDialog", "测试样本："))
        self.saveSampleDistributionChartLabel.setText(_translate("SampleMakerDialog", "样本分布图表："))
        self.saveSamplesResultPushButton.setText(_translate("SampleMakerDialog", "保存结果"))
        self.stepLogoLabel.setText(_translate("SampleMakerDialog", "TextLabel"))
        self.stepTipLabel.setText(_translate("SampleMakerDialog", "选择本地样本文件后，点击“下一步”以继续操作！"))
        self.previousStepPushButton.setText(_translate("SampleMakerDialog", "上一步"))
        self.nextStepPushButton.setText(_translate("SampleMakerDialog", "下一步"))
        self.cancelFinishPushButton.setText(_translate("SampleMakerDialog", "取消"))

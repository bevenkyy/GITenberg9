# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QGridLayout, QMessageBox, QHBoxLayout
import numpy as np

from utils.icons import get_icon, get_pixmap
from SampleMakerDialogDesigner import Ui_SampleMakerDialog
from fileio import ExcelIO
from data import SampleMaker
from chart.StatsChart import CoordinateAxis, LineChart, HistgramChart 


class SampleMakerDialog(QDialog, Ui_SampleMakerDialog):
    '''
    '''
    #
    qSetting = None
    #
    training_cv_samples = None
    test_samples = None


    def __init__(self, setting):
        super(SampleMakerDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.init_ui_element()
        self.init_sample_distribution_chart()
        #
        self.qSetting = setting
        self.all_samples = None
        self.features = None
        self.training_cv_samples = None
        self.test_samples = None
        #
        self.connect_singal_solt()
    
    def init_ui_element(self):
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        # ===================================================init all pages button icon=========================================================
        self.selectAllSamplePushButton.setIcon(get_icon("open_file"))
        self.saveTrainingCVSamplePushButton.setIcon(get_icon("save_file"))
        self.saveTestSamplePushButton.setIcon(get_icon("save_file"))
        self.saveSampleDistributionChartPushButton.setIcon(get_icon("save_file"))
        self.saveSamplesResultPushButton.setIcon(get_icon("save_file"))

        self.previousStepPushButton.setIcon(get_icon("previous_step"))
        self.nextStepPushButton.setIcon(get_icon("next_step"))
        self.cancelFinishPushButton.setIcon(get_icon("operation_cancel"))
        # =========================================================init ui elments=========================================================
        self.ui_element = {"selectAllSamplePage":{"operationLogoLabel":get_pixmap("import_data"),
                                                "operationTitleLabel":"选择总体样本",
                                                "operationDescriptionLabel":"选择一个总体样本，用以作为划分训练-验证样本和测试样本的数据源。",
                                                "stepLogoLabel":get_pixmap("info_tip"),
                                                "stepTipLabel":"选择总体样本数据文件后，点击“下一步”以继续操作。这里可查看样本特征的分布特性。"},
                            "setParameterPage":{"operationLogoLabel":get_pixmap("set_parameter"),
                                                "operationTitleLabel":"创建样本",
                                                "operationDescriptionLabel":"设置从总体样本创建、预处理训练-验证样本和测试样本数据的参数。",
                                                "stepLogoLabel":get_pixmap("info_tip"),
                                                "stepTipLabel":"设置划分训练验证样本和测试样本的比例、划分方法等参数后，点击“下一步”以继续操作！"},
                            "saveEstimatorDataPage":{"operationLogoLabel":get_pixmap("export_data"),
                                                "operationTitleLabel":"保存样本",
                                                "operationDescriptionLabel":"将创建并处理好的样本数据保存到本地。",
                                                "stepLogoLabel":get_pixmap("info_tip"),
                                                "stepTipLabel":"点击“保存结果”按钮以保存勾选的数据，点击“完成”按钮以关闭窗口！"}}
        self.update_ui_element(self.sampleMakerStackedWidget.currentWidget().objectName())

    def update_ui_element(self, stackedWidget_page_name):
        ui_element_dict = self.ui_element.get(stackedWidget_page_name)
        #
        self.operationLogoLabel.setPixmap(ui_element_dict.get("operationLogoLabel"))
        self.operationTitleLabel.setText(ui_element_dict.get("operationTitleLabel"))
        self.operationDescriptionLabel.setText(ui_element_dict.get("operationDescriptionLabel"))
        self.stepLogoLabel.setPixmap(ui_element_dict.get("stepLogoLabel"))
        self.stepTipLabel.setText(ui_element_dict.get("stepTipLabel"))

    def connect_singal_solt(self):
        self.selectAllSamplePushButton.clicked.connect(self.selectAllSamplePushButtonClicked)
        self.allSampleTypeComboBox.currentIndexChanged.connect(self.allSampleTypeComboBoxCurrentIndexChanged)

        self.makeSamplePushButton.clicked.connect(self.makeSamplePushButtonClicked)
        self.saveTrainingCVSamplePushButton.clicked.connect(self.saveTrainingCVSamplePushButtonClicked)
        self.saveTestSamplePushButton.clicked.connect(self.saveTestSamplePushButtonClicked)
        self.saveSamplesResultPushButton.clicked.connect(self.saveSamplesResultPushButtonClicked)

        self.previousStepPushButton.clicked.connect(self.previousStepPushButtonClicked)
        self.nextStepPushButton.clicked.connect(self.nextStepPushButtonClicked)
        self.cancelFinishPushButton.clicked.connect(self.cancelFinishPushButtonClicked)
    
    def init_sample_distribution_chart(self):
        #
        self.allSampleDistributionQHorizonatalBox = QHBoxLayout(self.allSampleDistributionFrame)
        self.allSampleDistributionQHorizonatalBox.setContentsMargins(0, 10, 0, 10)
        self.all_samples_axis = CoordinateAxis(title="总体样本分布图") 
        self.allSampleDistributionQHorizonatalBox.addWidget(self.all_samples_axis)

        self.trainingCvTestSampleDistributionGridLayout = QGridLayout(self.trainingCvTestSampleDistributionFrame)
        self.training_cv_samples_axis = CoordinateAxis(title="训练-验证样本分布图")
        self.trainingCvTestSampleDistributionGridLayout.addWidget(self.training_cv_samples_axis, 0,0,1,1)
        self.test_samples_axis = CoordinateAxis(title="测试样本分布图") 
        self.trainingCvTestSampleDistributionGridLayout.addWidget(self.test_samples_axis, 0,1,1,1)

    def selectAllSamplePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个测试总体样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectAllSampleLineEdit.setText(file_path)
            #
            if self.isIncludeRowTitleCheckBox.isChecked() and self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = True
                isIncludeColTitle = True
            if not self.isIncludeRowTitleCheckBox.isChecked() and self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = False
                isIncludeColTitle = True
            if self.isIncludeRowTitleCheckBox.isChecked() and not self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = True
                isIncludeColTitle = False
            if not self.isIncludeRowTitleCheckBox.isChecked() and not self.isIncludeColTitleCheckBox.isChecked():
                isIncludeRowTitle = False
                isIncludeColTitle = False
            #
            try:
                self.all_samples = ExcelIO.read_excel(file_path, 
                                                has_row_labels = isIncludeRowTitle,
                                                has_col_labels = isIncludeColTitle)
                self.count_samples = self.all_samples.shape[0]
                self.count_features = self.all_samples.shape[1] - 1
                self.count_nan = 0 #len(self.all_samples[np.isnan(self.all_samples)])
                self.features = self.all_samples[:, -1]

                self.countAllSamplesLabel.setText(str(self.count_samples))
                self.countFeaturesLabel.setText(str(self.count_features))
                self.countNanLabel.setText(str(self.count_nan))

                if self.allSampleTypeComboBox.currentIndex() == 0:
                    self.all_samples_stats_chart = HistgramChart(self.features.astype(np.float64), title = "总体样本分布图")
                else:
                    self.all_samples_stats_chart = LineChart(self.features.astype(np.float64), title = "总体样本分布图")
                self.allSampleDistributionQHorizonatalBox.removeWidget(self.all_samples_axis)
                self.allSampleDistributionQHorizonatalBox.addWidget(self.all_samples_stats_chart)
            except Exception as read_file_err_Info:
                QMessageBox.critical(self, "错误", "读取文件时发生了错误！错误信息如下：\n" + str(read_file_err_Info), QMessageBox.Ok)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def allSampleTypeComboBoxCurrentIndexChanged(self):
        if self.features is not None:
            self.allSampleDistributionQHorizonatalBox.removeWidget(self.all_samples_stats_chart)
            if self.allSampleTypeComboBox.currentIndex() == 0:
                self.all_samples_stats_chart = HistgramChart(self.features.astype(np.float64), title = "总体样本分布图")
            else:
                self.all_samples_stats_chart = LineChart(self.features.astype(np.float64), title = "总体样本分布图")
            #
            self.allSampleDistributionQHorizonatalBox.addWidget(self.all_samples_stats_chart)

    def makeSamplePushButtonClicked(self):
        self.test_size = self.testSampleSizeDoubleSpinBox.value()
        try:
            # self.training_cv_samples, self.test_samples = SampleMaker.sklearn_trainval_test_split(excel_data.astype(np.float64), test_size)
            self.training_cv_samples, self.test_samples = SampleMaker.trainval_test_split(self.all_samples.astype(np.float64),
                                                                                        self.test_size)
            #
            self.training_cv_stats_Chart = HistgramChart(self.training_cv_samples[:,-1], 
                                                        title="训练-验证样本分布图")
            self.trainingCvTestSampleDistributionGridLayout.removeWidget(self.training_cv_samples_axis)
            self.trainingCvTestSampleDistributionGridLayout.addWidget(self.training_cv_stats_Chart, 0,0,1,1)
            #
            self.test_stats_Chart = HistgramChart(self.test_samples[:,-1], title="测试样本分布图") 
            self.trainingCvTestSampleDistributionGridLayout.removeWidget(self.test_samples_axis)
            self.trainingCvTestSampleDistributionGridLayout.addWidget(self.test_stats_Chart, 0,1,1,1)
        except Exception as split_sample_err_info:
            QMessageBox.critical(self, "错误", "创建样本时发生了错误！错误信息如下：\n" + str(split_sample_err_info), QMessageBox.Ok)

    def saveTrainingCVSamplePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存训练验证样本的文件名",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.saveTrainingCVSampleLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))
    
    def saveTestSamplePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存测试样本的文件名",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.saveTestSampleLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def saveSamplesResultPushButtonClicked(self):
        save_training_cv_Sample_file_path = self.saveTrainingCVSampleLineEdit.text()
        save_test_Sample_file_path = self.saveTestSampleLineEdit.text()
        #
        if save_training_cv_Sample_file_path != "" and save_test_Sample_file_path != "":
            training_cv_row_title = []
            test_row_title = []
            training_cv_test_col_title = ["ID"]
            for i in range(self.training_cv_samples.shape[0]):
                training_cv_row_title.append(i + 1)
            for i in range(self.test_samples.shape[0]):
                test_row_title.append(i + 1)
            for i in range(self.training_cv_samples.shape[1] - 1):
                training_cv_test_col_title.append("F" + str(i + 1))
            training_cv_test_col_title.append("Label")
            #
            try:
                ExcelIO.write_excel(save_training_cv_Sample_file_path, 
                                    ["training_cv_set",], 
                                    [self.training_cv_samples,],
                                    row_title = training_cv_row_title, 
                                    col_title = training_cv_test_col_title)
                ExcelIO.write_excel(save_test_Sample_file_path,
                                    ["test_set",], 
                                    [self.test_samples,],
                                    row_title = test_row_title, 
                                    col_title = training_cv_test_col_title)
                #
                if QMessageBox.information(self,"提示","已成功保存样本文件!", QMessageBox.Ok) == QMessageBox.Ok:
                    self.close()
            except Exception as write_file_err_info:
                QMessageBox.critical(self, "错误", "保存文件时发生了错误！错误信息如下：\n" + str(write_file_err_info), QMessageBox.Ok)
    
    def cancelFinishPushButtonClicked(self):
        #
        if self.sampleMakerStackedWidget.currentIndex() != 2:
            qdlg_result = QMessageBox.question(self, "询问", "样本尚未创建完成，是否仍关闭此窗口？", QMessageBox.Yes|QMessageBox.No)
            if qdlg_result == QMessageBox.No:
                return
            else:
                self.close()
        else:
            self.close()

    def previousStepPushButtonClicked(self):
        idx = self.sampleMakerStackedWidget.currentIndex()
        if idx == 1:
            self.previousStepPushButton.setEnabled(False)
            self.nextStepPushButton.setEnabled(True)
            self.sampleMakerStackedWidget.setCurrentIndex(idx - 1)
        if idx == 2:
            self.cancelFinishPushButton.setIcon(get_icon("operation_cancel"))
            self.cancelFinishPushButton.setText("取消")
            self.sampleMakerStackedWidget.setCurrentIndex(idx - 1)
        #
        # 更新各个页面上的提示文本
        stackedWidget_page_name = self.sampleMakerStackedWidget.widget(idx - 1).objectName()
        self.update_ui_element(stackedWidget_page_name)

    def nextStepPushButtonClicked(self):
        idx = self.sampleMakerStackedWidget.currentIndex()
        if idx == 0: 
            if self.all_samples is None:
                QMessageBox.critical(self, "错误", "未能成功读取总体样本数据，请检查输入文件是否正确！", QMessageBox.Yes)
                return
            else:
                self.sampleMakerStackedWidget.setCurrentIndex(idx + 1)
                self.previousStepPushButton.setEnabled(True)
        if idx == 1:
            if self.training_cv_samples is None or self.training_cv_samples is None:
                # 训练验证样本和测试样本必然是同时创建的，因此只用判断其中一个是否为空即可
                QMessageBox.critical(self, "错误", "训练-验证样本、测试样本尚未创建，无法进入下一步！", QMessageBox.Yes)
                return
            else:
                self.sampleMakerStackedWidget.setCurrentIndex(idx + 1)
                self.nextStepPushButton.setEnabled(False)
                self.cancelFinishPushButton.setText("完成")
                self.cancelFinishPushButton.setIcon(get_icon("finish_tip2"))
        #
        # 更新各个页面上的提示文本
        stackedWidget_page_name = self.sampleMakerStackedWidget.widget(idx + 1).objectName()
        self.update_ui_element(stackedWidget_page_name)

def main(setting):
    app = QApplication(sys.argv)
    sampleMakerDialog = SampleMakerDialog(setting)
    sampleMakerDialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)
    

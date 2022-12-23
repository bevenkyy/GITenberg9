# -*- coding:utf-8 -*-

import os
import sys

import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from fileio import ExcelIO, ModelIO
from utils.icons import get_icon
from data.FeatureProcessor import *
from utils import convert_data_structure
from chart.StatsChart import  CoordinateAxis, BarChart
from FeatureCreatorDialogDesigner import Ui_FeatureCreatorDialog

class FeatureCreatorDialog(QDialog, Ui_FeatureCreatorDialog):

    #
    qSetting = None
    #     
    sample = None
    feature_stats_info = {"variance":None,
                          "pearson_corrcoef":None,
                          "distance_corrcoef":None}

    def __init__(self, setting):
        super(FeatureCreatorDialog, self).__init__(None)
        self.setupUi(self)
        self.qSetting = setting
        #
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #
        #========singal and slot========
        self.selectOpenAllSamplesPushButton.clicked.connect(self.selectOpenAllSamplesPushButtonClicked)
        self.applySensitiveFeaturePushButton.clicked.connect(self.applySensitiveFeaturePushButtonClicked)
        self.selectSaveFeaturePushButton.clicked.connect(self.selectSaveFeaturePushButtonClicked)
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
        #

    def selectOpenAllSamplesPushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectOpenAllSamplesLineEdit.setText(file_path)
            self.sample = ExcelIO.read_excel(file_path)
            #
            initialization_features_str = get_initialization_feature(self.sample.shape[1] - 1)
            self.initializationFeatureLineEdit.setText(initialization_features_str)
        #
        self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def applySensitiveFeaturePushButtonClicked(self):
        #
        if self.sensitiveFeatureLineEdit.text() == "":
            QMessageBox.critical(self, "错误", "敏感波段不能为空!", QMessageBox.Ok)
            return
        else:
            if self.isCalculateOneFeatureRatioQCheckBox.isChecked() and \
                self.isCalculateTwoFeatureSumDifferenceRatioQCheckBox.isChecked():
                self.one_feature_ratio = parse_one_feature_ratio(self.sensitiveFeatureLineEdit.text())
                self.two_feature_sum_difference_ratio = parse_two_feature_sum_difference_ratio(self.sensitiveFeatureLineEdit.text())
                self.all_new_feature = self.one_feature_ratio + self.two_feature_sum_difference_ratio
            elif self.isCalculateOneFeatureRatioQCheckBox.isChecked():
                self.all_new_feature = parse_one_feature_ratio(self.sensitiveFeatureLineEdit.text())
            elif self.isCalculateTwoFeatureSumDifferenceRatioQCheckBox.isChecked():
                self.all_new_feature = parse_two_feature_sum_difference_ratio(self.sensitiveFeatureLineEdit.text())
            else:
                QMessageBox.critical(self, "提示", "单特征比值选项与双特征和差比值选项均未勾选，\
                                    因此程序不会生成任何新的特征!",
                                    QMessageBox.Ok)
                return
        #
        _translate = QtCore.QCoreApplication.translate
        self.generationFeatureLabel.setText(_translate("FeatureCreatorForm", "生成特征：" \
                                                + str(len(self.all_new_feature)) + "个"))
        self.generationFeatureListWidget.addItems(self.all_new_feature)

    def selectSaveFeaturePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectSaveFeatureLineEdit.setText(file_path)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def okPushButtonClicked(self):
        #
        sensitive_feature_str = self.sensitiveFeatureLineEdit.text()
        custom_feature = self.customFeaturePlainTextEdit.toPlainText().split("\n")
        if len(custom_feature[0]) > 0:
            self.all_new_feature =self.all_new_feature + custom_feature
        #
        new_sample, col_title = feature_calculator(self.sample, sensitive_feature_str, self.all_new_feature)
        #
        if self.isMergeInitNewFeatureCheckBox.isChecked():
            sensitive_sample_dict = make_feature(self.sample, sensitive_feature_str)
            sensitive_sample, sensitive_col_title = convert_data_structure.dict_to_2darray(sensitive_sample_dict,
                                                                                          None)
            save_sample = np.hstack((new_sample, sensitive_sample))
            col_title = ["ID",] + col_title + sensitive_col_title
        else:
            save_sample = new_sample
        #
        row_title = [i for i in range(1, save_sample.shape[0] + 1)]
        ExcelIO.write_excel(self.selectSaveFeatureLineEdit.text(), ["new_sample",], [save_sample,], row_title, col_title)
        QMessageBox.information(self, "提示", "已保存构建的特征！", QMessageBox.Ok)
        self.close()

    def cancelPushButtonClicked(self):
        #
        self.close()

def main(setting):
    app = QApplication(sys.argv)
    featureCreatorDialog = FeatureCreatorDialog(setting)
    featureCreatorDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

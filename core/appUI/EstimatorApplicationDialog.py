# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from EstimatorApplicationDialogDesigner import Ui_EstimatorApplicationDialog

from InitResource import get_icon, get_pixmap, get_gif
from fileIO import ModelIO
from model import ModelApplication

class EstimatorApplicationDialog(QDialog, Ui_EstimatorApplicationDialog):
    '''
    '''
    #
    qSetting = None
    model_application = []
    
    def __init__( self, setting ):
        super(EstimatorApplicationDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.init_ui_element()
        #
        self.qSetting = setting
        #
        self.selectDataFilePushButton.clicked.connect(self.selectDataFilePushButtonClicked)
        self.delDataFilePushButton.clicked.connect(self.delDataFilePushButtonClicked)
        self.clearDataFilePushButton.clicked.connect(self.clearDataFilePushButtonClicked)
        self.selectModelFilePushButton.clicked.connect(self.selectModelFilePushButtonClicked)
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)
        #

    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("tool_ToolBoxTreeWidget"))
        #
        self.selectDataFilePushButton.setIcon(get_icon("open_file"))
        self.clearDataFilePushButton.setIcon(get_icon("clear_file"))
        self.delDataFilePushButton.setIcon(get_icon("del_file"))
        self.selectModelFilePushButton.setIcon(get_icon("select_folder"))
        #
        self.fileListTableWidget.setHorizontalHeaderLabels(("待预测数据", "预测数据"))
        self.fileListTableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)  #选中列还是行，这里设置选中行
        self.fileListTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) 
        # self.fileListTableWidget.horizontalHeader().setStretchLastSection(True) #列宽度占满表格(最后一个列拉伸处理沾满表格)
        self.fileListTableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.fileListTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.fileListTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

    def selectDataFilePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path_list, _ =  QFileDialog.getOpenFileNames(self, "打开一个或多个待预测的数据文件",
                                                          lastFileDir,
                                                          "GeoTiff文件(*.tif *.TIF);;Excel文件(*.xlsx)")
        if len(file_path_list) > 0:
            #
            for i, file_path in enumerate(file_path_list):
                if i + 1 > self.fileListTableWidget.rowCount():
                    self.fileListTableWidget.setRowCount(self.parameterListTableWidget.rowCount() + 5)
                for row_index in range(self.fileListTableWidget.rowCount()):
                    if self.fileListTableWidget.item(row_index, 0) == None:
                        self.fileListTableWidget.setItem(row_index, 0, QTableWidgetItem(file_path))
                        out_file_path = os.path.splitext(file_path)[0] + "_fit_" + str(row_index + 1) + os.path.splitext(file_path)[1]
                        self.fileListTableWidget.setItem(row_index, 1, QTableWidgetItem(out_file_path))
                        break
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path_list[0]))
                    
    def delDataFilePushButtonClicked(self):
        self.fileListTableWidget.removeRow(self.fileListTableWidget.currentRow())
        self.fileListTableWidget.setRowCount(self.fileListTableWidget.rowCount() + 1)

    def clearDataFilePushButtonClicked(self):
        self.fileListTableWidget.clearContents()

    def selectModelFilePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "打开一个模型文件",
                                                   lastFileDir,
                                                    "json文件(*.json)")
        if file_path != "":
            self.selectModelFileLineEdit.setText(file_path)
            estimator_info_text = ""
            #
            trained_estimator_info = ModelIO.load_estimator(file_path)
            #
            self.estimator_name = trained_estimator_info.get("estimator_name")
            self.training_samples_count = trained_estimator_info.get("training_samples_count")
            self.test_samples_count = trained_estimator_info.get("test_samples_count")
            self.cv = trained_estimator_info.get("cv")
            self.samples_features = trained_estimator_info.get("samples_features")
            self.params_type = trained_estimator_info.get("params_type")
            self.trained_estimator = trained_estimator_info.get("trained_estimator")
            #
            estimator_name_str = "模型:" + self.estimator_name + "\n"
            training_samples_count_str = "训练样本容量:" + str(self.training_samples_count) + "\n"
            test_samples_count_str = "测试样本容量:" + str(self.test_samples_count) + "\n"
            samples_feature_str = "样本特征:" + self.samples_features + "\n"
            #
            if self.params_type == "tuning":
                cv_str = "交叉验证:" + self.cv + "\n"
                estimator_params_str = "模型参数:" + str(self.trained_estimator.get_params()) + "\n"
                #
                estimator_info_text += estimator_name_str + '\n' + str(training_samples_count_str) + '\n' \
                                    + str(test_samples_count_str) + '\n' + samples_feature_str + '\n'\
                                    + cv_str + estimator_params_str
            else:
                estimator_params_str = "模型参数:" + str(self.trained_estimator.get_params()) + "\n"
                #
                estimator_info_text += estimator_name_str + '\n' + str(training_samples_count_str) + '\n' \
                                    + str(test_samples_count_str) + '\n' + samples_feature_str + '\n'\
                                    + estimator_params_str
            #
            self.modelInfoTextBrowser.setPlainText(estimator_info_text)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    def okPushButtonClicked(self):
        self.fit_gif = get_gif("fit_model")
        self.statusLogoLabel.setMovie(self.fit_gif)
        self.fit_gif.start()
        self.statusTipLabel.setText("正在应用模型，请稍后！")
        #  
        true_data_file_path_list = []
        pred_data_file_path_list = []
        for row_index in range(self.fileListTableWidget.rowCount()):
            if self.fileListTableWidget.item(row_index, 0) == None:
                break
            else:
                true_data_file_path_list.append(self.fileListTableWidget.item(row_index, 0).text())
                pred_data_file_path_list.append(self.fileListTableWidget.item(row_index, 1).text())
        #
        if self.isUnifyFeaturesCheckBox.isChecked():
            self.unify_features = True
        else:
            self.unify_features = False
        #
        self.fit_img_thread = RunThread(self.trained_estimator,
                                        true_data_file_path_list, pred_data_file_path_list,
                                        self.samples_features, self.unify_features)
        self.fit_img_thread.updateFinishedStatus_signal.connect(self.updateFinishedStatus)
        self.fit_img_thread.start()  


    def updateFinishedStatus(self):
        self.statusLogoLabel.setPixmap(get_pixmap("finish_tip1"))
        self.statusTipLabel.setText("数据预测完成！")
        #
        if QMessageBox.information(self,"提示","已完成数据预测!", QMessageBox.Ok) == QMessageBox.Ok:
            self.close()

    def cancelPushButtonClicked(self):
        self.close()


class RunThread(QtCore.QThread):

    updateFinishedStatus_signal = QtCore.pyqtSignal()

    def __init__(self, trained_model, true_img_file_path_list, pred_img_file_path_list,  sample_feature, unify_features):
        super().__init__()
        self.trained_model = trained_model
        self.true_img_file_path_list = true_img_file_path_list
        self.pred_img_file_path_list = pred_img_file_path_list
        self.sample_feature = sample_feature
        self.unify_features = unify_features

    def run(self):
        for true_img_file_path, pred_img_file_path in zip(self.true_img_file_path_list, self.pred_img_file_path_list):
            ModelApplication.apply_model_by_img(self.trained_model, 
                                                true_img_file_path, pred_img_file_path, 
                                                self.sample_feature, self.unify_features)
        #
        self.updateFinishedStatus_signal.emit()
        
        
def main(setting):
    app = QApplication(sys.argv)
    modelApplicationDialog = ModelApplicationDialog(setting)
    modelApplicationDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

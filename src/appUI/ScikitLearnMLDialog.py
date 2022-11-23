# -*- coding:utf-8 -*-

import os
import sys
from multiprocessing import Process, Manager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import multiprocessing
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem

from InitResource import get_icon, get_pixmap, get_gif
from fileIO import ExcelIO, ModelIO
from ScikitLearnMLDialogDesigner import Ui_ScikitLearnMLDialog
from model.ScikitLearnML import ScikitLearnML
from chart.StatsChart import CoordinateAxis, BarChart, HistgramChart
from ChartViewDialog import ChartViewDialog


class ScikitLearnMLDialog(QDialog, Ui_ScikitLearnMLDialog):

    def __init__(self, setting):
        super(ScikitLearnMLDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        self.qTranslate = QtCore.QCoreApplication.translate
        #
        self.params_filepath = str(self.qSetting.value("sklearnParamsFilepath"))
        #
        self.training_cv_samples = None
        self.training_cv_samples_features = None
        self.test_samples = None
        self.test_samples_features = None
        #
        self.task_type = ""
        self.estimator_name = ""
        self.estimator = ""
        self.params_type = None
        self.params_info = None
        self.basic_params = None
        self.training_params = {"cv":5, "n_jobs":2}
        #
        self.training_info = ""
        #
        self.trained_estimator = None
        self.trained_data = None
        self.cv_data = None
        self.test_data = None
        #
        self.training_size = None
        self.training_scores = None
        self.cv_scores = None
        #
        #========init dialog========
        self.init_global_UI_element()
        self.init_selectTaskPage_UI_element()
        #==============================================tmp==============================================
        self.selectParameterTunerLabel.setEnabled(False)
        self.selectParameterTunerComboBox.setEnabled(False)
        self.resetParameterPushButton.setEnabled(False)
        self.saveParameterToFilePushButton.setEnabled(False)
        #==============================================tmp==============================================
        #
        self.connect_singal_solt()

    def connect_singal_solt(self):
        #========singal and slot========
        self.selectTrainingValidationSamplePushButton.clicked.connect(self.selectTrainingValidationSamplePushButtonClicked)
        self.selectTestSamplePushButton.clicked.connect(self.selectTestSamplePushButtonClicked)

        self.selectEstimatorComboBox.currentIndexChanged.connect(self.selectEstimatorComboBoxCurrentIndexChanged)
        self.selectParameterTypeComboBox.currentIndexChanged.connect(self.selectParameterTypeComboBoxCurrentIndexChanged)
        self.basicParameterTableWidget.itemChanged.connect(self.basicParameterTableWidgetItemChanged)

        self.kFoldCVLineEdit.editingFinished.connect(self.kFoldCVLineEditEditingFinished)
        self.nJobsComboBox.currentIndexChanged.connect(self.nJobsCurrentIndexChanged)
        self.trainEstimatorPushButton.clicked.connect(self.trainEstimatorPushButtonClicked)
        self.estimatorLearningCurveChartPushButton.clicked.connect(self.estimatorLearningCurveChartPushButtonClicked)
        self.estimatorEvaluationChartPushButton.clicked.connect(self.estimatorEvaluationChartPushButtonClicked)

        self.isSaveBestEstimatorToFileCheckBox.clicked.connect(self.isSaveBestEstimatorToFileCheckBoxClicked)
        self.isSaveEstimatorDataToExcelFileNameCheckBox.clicked.connect(self.isSaveEstimatorDataToExcelFileNameCheckBoxClicked)
        self.selectEstimatorDataSaveDirectoryPushButton.clicked.connect(self.selectEstimatorDataSaveDirectoryPushButtonClicked)
        self.resetSaveParameterPushButton.clicked.connect(self.resetSaveParameterPushButtonClicked)
        self.saveEstimatorDataPushButton.clicked.connect(self.saveEstimatorDataPushButtonClicked)

        self.previousStepPushButton.clicked.connect(self.previousStepPushButtonClicked)
        self.nextStepPushButton.clicked.connect(self.nextStepPushButtonClicked)
        self.cancelFinishPushButton.clicked.connect(self.cancelFinishPushButtonClicked)

    def init_global_UI_element(self):
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        # ===================================================init all pages button icon=========================================================
        self.selectTrainingValidationSamplePushButton.setIcon(get_icon("open_file"))
        self.selectTestSamplePushButton.setIcon(get_icon("open_file"))
        self.importParameterFromFilePushButton.setIcon(get_icon("open_file"))
        self.resetParameterPushButton.setIcon(get_icon("reset_parameter"))
        self.saveParameterToFilePushButton.setIcon(get_icon("save_file"))
        self.trainEstimatorPushButton.setIcon(get_icon("train_model2"))
        self.selectEstimatorDataSaveDirectoryPushButton.setIcon(get_icon("select_folder"))
        self.resetSaveParameterPushButton.setIcon(get_icon("reset_parameter"))
        self.saveEstimatorDataPushButton.setIcon(get_icon("save_file"))
        self.previousStepPushButton.setIcon(get_icon("previous_step"))
        self.nextStepPushButton.setIcon(get_icon("next_step"))
        self.cancelFinishPushButton.setIcon(get_icon("operation_cancel"))
        # =========================================================init ui elments=========================================================
        self.ui_element = {"selectTaskTypePage":{"operationLogoLabel":get_pixmap("select_task"),
                                                "operationTitleLabel":"选择任务",
                                                "operationDescriptionLabel":"根据问题，选择对应的机器学习的模式类型，这里提供了分类模型、回归模型和聚类模型三大类机器学习常见的模型。",
                                                "stepLogoLabel":get_pixmap("info_tip"),
                                                "stepTipLabel":"选择要训练的机器学习模型所属的类型后，点击“下一步”以继续操作！"},
                            "selectSamplePage":{"operationLogoLabel":get_pixmap("import_data"),
                                                "operationTitleLabel":"选择样本",
                                                "operationDescriptionLabel":"选择训练、调试模型所用的训练验证数据集以及评估模型泛化性的测试集。",
                                                "stepLogoLabel":get_pixmap("info_tip"),
                                                "stepTipLabel":"选择本地训练验证样本（和测试样本）文件后，点击“下一步”以继续操作！"},
                            "setParameterPage":{"operationLogoLabel":get_pixmap("set_parameter"),
                                                "operationTitleLabel":"设置参数",
                                                "operationDescriptionLabel":"选择机器学习所要解决的任务类型、学习器并设置或从文件导入学习器参数。",
                                                "stepLogoLabel":get_pixmap("info_tip"),
                                                "stepTipLabel":"设置模型参数及要调试的参数后，点击“下一步”以继续操作！"},
                            "trainEstimatorPage":{"operationLogoLabel":get_pixmap("train_model1"),
                                              "operationTitleLabel":"训练模型",
                                              "operationDescriptionLabel":" 训练并对模型进行交叉验证，训练完毕后，查看模型的训练过程统计图表及测试集上的评估图表（如果输入了测试集）。",
                                              "stepLogoLabel":get_pixmap("info_tip"),
                                              "stepTipLabel":"点击“训练”按钮，待模型训练完毕后，点击“下一步”以继续操作！"},
                            "saveEstimatorDataPage":{"operationLogoLabel":get_pixmap("export_data"),
                                                 "operationTitleLabel":"导出数据",
                                                 "operationDescriptionLabel":"保存训练好的模型，同时可选择保存模型训练、验证及测试（如果输入了测试集）过程中产生的数据。",
                                                 "stepLogoLabel":get_pixmap("info_tip"),
                                                 "stepTipLabel":"勾选要保存的数据并修改对应名称,点击“保存结果”按钮以保存勾选的数据，点击“完成”按钮以关闭窗口！"}}

    def init_selectTaskPage_UI_element(self):
        self.update_ui_element(self.scikitLearnSettingStackedWidget.currentWidget().objectName())
        self.classificationIconLabel.setPixmap(get_pixmap("classifier_icon"))
        self.regressionIconLabel.setPixmap(get_pixmap("regressor_icon"))
        self.clusterIconLabel.setPixmap(get_pixmap("clusterer_icon"))

    def get_task_type(self):
        if self.classificationTaskRadioButton.isChecked():
            _task_type = "Classification"
        elif self.regressionTaskRadioButton.isChecked():
            _task_type = "Regression"
        else:
            _task_type = "Cluster"
        #
        return _task_type

    def init_selectSamplePage_UI_element(self):
        self.training_cv_samples = None
        self.test_samples = None
        self.selectTrainingValidationSampleLineEdit.setText(None)
        self.selectTestSampleLineEdit.setText(None)
        for i in range(self.sampleStatisticChartGridLayout.count()):
            self.sampleStatisticChartGridLayout.itemAt(i).widget().deleteLater()
        #
        self.training_val_sample_axis_chart = CoordinateAxis()
        self.test_sample_axis_chart = CoordinateAxis()
        self.sampleStatisticChartGridLayout.addWidget(self.training_val_sample_axis_chart,0,0,1,1)
        self.sampleStatisticChartGridLayout.addWidget(self.test_sample_axis_chart,0,1,1,1)

    def init_setParameterPage_UI_element(self):
        self.selectEstimatorComboBox.clear()
        validEstimator = ModelIO.query_estimator_name(self.params_filepath, estimator_type = self.task_type)
        for _estimator_name in validEstimator:
            self.selectEstimatorComboBox.addItem(self.qTranslate("ScikitLearnMLDialog", _estimator_name))
        # if self.selectEstimatorComboBox.count() > 0:
        #     if is_update:
        #         self.selectEstimatorComboBox.clear()
        #         validEstimator = ModelIO.query_estimator_name(self.params_filepath, estimator_type = self.task_type)
        #         for _estimator_name in validEstimator:
        #             self.selectEstimatorComboBox.addItem(self.qTranslate("ScikitLearnMLDialog", _estimator_name))
        #     else:
        #         validEstimator = ModelIO.query_estimator_name(self.params_filepath, estimator_type = self.task_type)
        #         for _estimator_name in validEstimator:
        #             self.selectEstimatorComboBox.addItem(self.qTranslate("ScikitLearnMLDialog", _estimator_name))
        # else:
        #     pass

    def init_trainEstimatorPage_UI_element(self):
        self.nJobsItem = [str(count + 1) for count in range(multiprocessing.cpu_count())]
        self.nJobsComboBox.addItems(self.nJobsItem)
        self.nJobsComboBox.setCurrentIndex(len(self.nJobsItem) - 3)
        if self.task_type == "Classification" or self.task_type == "Cluster":
            self.estimatorScore_1Label.setText("OA")
            self.estimatorScore_2Label.setText("Kappa系数")
        else:
            self.estimatorScore_1Label.setText("R2")
            self.estimatorScore_2Label.setText("RMSE")

    def init_saveEstimatorDataPage_UI_element(self):
        self.isSaveBestEstimatorToFileLineEdit.setText(self.estimator + "_Best_Parameters_Estimator.json")
        self.isSaveEstimatorDataToExcelFileNameLineEdit.setText(self.estimator + "_Estimator_Data.xlsx")
        self.isSaveTrainingDataToWorkingSheetNameLineEdit.setText(self.estimator + "_Training")
        self.isSaveCVDataToWorkingSheetNameLineEdit.setText(self.estimator + "_CrossValidation")
        self.isSaveTestDataToWorkingSheetNameLineEdit.setText(self.estimator + "_Test")
        #
        self.isSaveBestEstimatorToFileCheckBox.setEnabled(True)
        self.isSaveEstimatorDataToExcelFileNameCheckBox.setEnabled(True)
        self.isSaveTrainingDataToWorkingSheetNameCheckBox.setEnabled(True)
        self.isSaveTrainingDataToWorkingSheetNameCheckBox.setChecked(True)
        if self.params_type is not None and self.params_type != "default":
            self.isSaveCVDataToWorkingSheetNameCheckBox.setEnabled(True)
            self.isSaveCVDataToWorkingSheetNameCheckBox.setChecked(True)
            self.isSaveCVDataToWorkingSheetNameLineEdit.setEnabled(True)
        if self.test_samples is not None:
            self.isSaveTestDataToWorkingSheetNameCheckBox.setEnabled(True)
            self.isSaveTestDataToWorkingSheetNameCheckBox.setChecked(True)
            self.isSaveTestDataToWorkingSheetNameLineEdit.setEnabled(True)
        #
        self.isSaveTrainingDataToWorkingSheetNameCheckBox.blockSignals(False)
        self.isSaveCVDataToWorkingSheetNameCheckBox.blockSignals(False)
        self.isSaveTestDataToWorkingSheetNameCheckBox.blockSignals(False)

    def update_ui_element(self, stackedWidget_page_name):
        #
        ui_element_dict = self.ui_element.get(stackedWidget_page_name)
        #
        self.operationLogoLabel.setPixmap(ui_element_dict.get("operationLogoLabel"))
        self.operationTitleLabel.setText(ui_element_dict.get("operationTitleLabel"))
        self.operationDescriptionLabel.setText(ui_element_dict.get("operationDescriptionLabel"))
        self.stepLogoLabel.setPixmap(ui_element_dict.get("stepLogoLabel"))
        self.stepTipLabel.setText(ui_element_dict.get("stepTipLabel"))

    def update_basic_params(self):
        #
        self.estimator_name = self.selectEstimatorComboBox.currentText()
        self.estimator = ModelIO.query_estimator(self.params_filepath, 
                                                 estimator_name = self.estimator_name,
                                                 estimator_type = self.task_type)
        #
        params_type_text = self.selectParameterTypeComboBox.currentText()
        if params_type_text == "默认参数":
            self.params_type = "default"
        elif params_type_text == "调试参数":
            self.params_type = "tuning"
        else:
            self.params_type = "custom"
        #
        self.params_info = ModelIO.read_sklearn_params_from_json(self.params_filepath,
                                                                 self.estimator,
                                                                 params_type = self.params_type)
        self.basic_params = self.params_info[2]
        for i, (params_name, params_value) in enumerate(self.params_info[1].items()):
            item = QTableWidgetItem(self.qTranslate("ScikitLearnMLDialog", params_name))
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.basicParameterTableWidget.setItem(i, 0,item)
            item = QTableWidgetItem(self.qTranslate("ScikitLearnMLDialog", params_value))
            self.basicParameterTableWidget.setItem(i, 1,item)

    def update_training_params(self):
        self.training_params["cv"] = int(self.kFoldCVLineEdit.text())
        self.training_params["n_jobs"] = int(self.nJobsComboBox.currentText())

    def update_training_info(self):
        #
        self.preTrainingEstimatorInfoTextBrowser.clear()
        #
        self.training_info = "训练-验证样本信息：\n"
        self.training_info += "样本数：" + str(self.training_cv_samples.shape[0]) + "\n"
        self.training_info += "特征数：" + str(self.training_cv_samples.shape[1]) + "\n"
        self.training_info += "特征：" + ','.join(self.training_cv_samples_features.tolist()) + \
                              "\n\n------------------------------------------------------\n\n"
        #
        self.training_info += "测试样本信息：\n"
        if self.test_samples is not None:
            self.training_info += "样本数：" + str(self.test_samples.shape[0]) + "\n"
            self.training_info += "特征数：" + str(self.test_samples.shape[1]) + "\n"
            self.training_info += "特征：" + ','.join(self.test_samples_features.tolist()) + \
                                  "\n\n------------------------------------------------------\n\n"
        else:
            self.training_info += "样本数：0\n"
            self.training_info += "特征数：0\n"
            self.training_info += "特征：\n\n----------------------------------------------------------\n\n"
        #
        self.training_info += "学习器：" + self.estimator_name  + "\n" + \
                              "\n基本参数：\n"
        #
        for param_name, param_value in self.params_info[1].items():
            self.training_info += param_name + "：" + param_value + "\n"
        # 
        self.training_info +=  "\n训练参数：\n"
        for param_name, param_value in self.training_params.items():
            param_value = str(param_value)
            self.training_info += param_name + "：" + param_value + "\n" 
        #
        self.preTrainingEstimatorInfoTextBrowser.setPlainText(self.training_info)

    # =========================================================Select Sample Data Page=========================================================

    def selectTrainingValidationSamplePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个测试样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectTrainingValidationSampleLineEdit.setText(file_path)
            #
            self.training_cv_samples = ExcelIO.read_excel(file_path,  
                                                          has_row_labels= True, has_col_labels = True).astype(np.float64)
            self.training_cv_samples_features = ExcelIO.read_excel_row(file_path)[1:-1]
            #
            if self.task_type == "Classification" or self.task_type == "Cluster":
                training_val_sample_stats_chart = BarChart(self.training_cv_samples[:,-1], 
                                                           title="Training Cross-Validation Samples Bar")
                self.sampleStatisticChartGridLayout.removeWidget(self.training_val_sample_axis_chart)
                # self.sampleStatisticChartGridLayout.itemAt(0).widget().deleteLater()
            elif self.task_type == "Regression":
                training_val_sample_stats_chart = HistgramChart(self.training_cv_samples[:,-1], 
                                                                title="Training Cross-Validation Samples Histogram")
                self.sampleStatisticChartGridLayout.removeWidget(self.training_val_sample_axis_chart)
                # self.sampleStatisticChartGridLayout.itemAt(0).widget().deleteLater()
            else:
                pass
            #
            self.sampleStatisticChartGridLayout.addWidget(training_val_sample_stats_chart,0,0,1,1)
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))
            self.nextStepPushButton.setEnabled(True)

    def selectTestSamplePushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getOpenFileName(self, "选择一个测试样本文件",
                                                    lastFileDir,
                                                    "Excel文件(*.xlsx)")
        if file_path != "":
            self.selectTestSampleLineEdit.setText(file_path)
            #
            self.test_samples = ExcelIO.read_excel(file_path,  
                                                   has_row_labels= True, has_col_labels = True).astype(np.float64)
            self.test_samples_features = ExcelIO.read_excel_row(file_path)[1:-1]
            #
            if self.task_type == "Classification" or self.task_type == "Cluster":
                test_sample_stats_chart = BarChart(self.test_samples[:,-1].astype(np.float64), 
                                                   title="Test Samples Bar")
                self.sampleStatisticChartGridLayout.removeWidget(self.test_sample_axis_chart)
                # self.sampleStatisticChartGridLayout.itemAt(1).widget().deleteLater()
            elif self.task_type == "Regression":
                test_sample_stats_chart = HistgramChart(self.test_samples[:,-1].astype(np.float64), 
                                                        title="Test Samples Histogram")
                self.sampleStatisticChartGridLayout.removeWidget(self.test_sample_axis_chart)
                # self.sampleStatisticChartGridLayout.itemAt(1).widget().deleteLater()
            else:
                pass
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))
            self.sampleStatisticChartGridLayout.addWidget(test_sample_stats_chart,0,1,1,1)
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

    # =========================================================Set Model Parameter Page=========================================================

    def selectEstimatorComboBoxCurrentIndexChanged(self):
        #
        self.estimatorLearningCurveChartPushButton.setEnabled(False)
        self.estimatorEvaluationChartPushButton.setEnabled(False)
        #
        self.basicParameterTableWidget.blockSignals(True)
        #
        self.basicParameterTableWidget.clearContents()
        self.update_basic_params()
        #
        self.basicParameterTableWidget.blockSignals(False)

    def selectParameterTypeComboBoxCurrentIndexChanged(self):
        #
        self.estimatorLearningCurveChartPushButton.setEnabled(False)
        self.estimatorEvaluationChartPushButton.setEnabled(False)
        #
        self.basicParameterTableWidget.blockSignals(True)
        #
        self.basicParameterTableWidget.clearContents()
        self.update_basic_params()
        #
        self.basicParameterTableWidget.blockSignals(False)

    def basicParameterTableWidgetItemChanged(self):
        #
        self.estimatorLearningCurveChartPushButton.setEnabled(False)
        self.estimatorEvaluationChartPushButton.setEnabled(False)
        #
        changed_params_name_item = self.basicParameterTableWidget.item(self.basicParameterTableWidget.currentRow(),0)
        changed_params_value_item = self.basicParameterTableWidget.item(self.basicParameterTableWidget.currentRow(),1)
        if changed_params_name_item is not None and changed_params_value_item is not None:
            changed_params_name = changed_params_name_item.text()
            changed_params_value = changed_params_value_item.text()
            #
            new_params_value = []
            for param in changed_params_value.split(','):
                try:
                    new_params_value.append(eval(param))
                except NameError:
                    new_params_value.append(param)
        #
        self.basic_params[self.params_info[0].get(changed_params_name)] = new_params_value
        self.params_info[1][changed_params_name] = changed_params_value

    # =========================================================Train Model Data Page=========================================================

    def kFoldCVLineEditEditingFinished(self):
        #
        kFold_value_str = self.kFoldCVLineEdit.text()
        try:
            kFold_value = int(kFold_value_str)
            if kFold_value > self.training_cv_samples.shape[0]:
                QMessageBox.critical(self, "错误", '''"交叉验证参数"的K值应该小于等于“训练-验证样本”数！''', QMessageBox.Ok)
                self.kFoldCVLineEdit.clear()
            else:
                self.update_training_params()
                self.update_training_info()
        except ValueError:
            QMessageBox.critical(self, "错误", '''"交叉验证参数"的K值应该设置为一个有效的正整数！''', QMessageBox.Ok)
            self.kFoldCVLineEdit.clear()

    def nJobsCurrentIndexChanged(self):
        #
        self.update_training_params()
        self.update_training_info()

    def trainEstimatorPushButtonClicked(self):
        #
        if self.kFoldCVLineEdit.text() == "":
            QMessageBox.critical(self, "错误", '''未设置“交叉验证参数”的K值！''', QMessageBox.Ok)
        else:
            self.trainEstimatorPushButton.setEnabled(False)
            self.previousStepPushButton.setEnabled(False)
            self.nextStepPushButton.setEnabled(False)
            self.estimatorLearningCurveChartPushButton.setEnabled(False)
            self.estimatorEvaluationChartPushButton.setEnabled(False)
            #
            fit_gif = get_gif("fit_model")
            self.stepLogoLabel.setPixmap(QtGui.QPixmap(""))
            self.stepLogoLabel.setMovie(fit_gif)
            fit_gif.start()
            self.stepTipLabel.setText("正在训练模型,请稍后！")
            #
            print(self.estimator)
            self.fit_thread = RunFitEstimatorThread(self.training_cv_samples, self.test_samples,
                                                    self.task_type, self.estimator, 
                                                    self.params_type, self.basic_params, self.training_params)
            self.fit_thread.update_estimator_data_signal.connect(self.update_estimator_data)
            self.fit_thread.start()     

    def update_estimator_data(self, return_estimator_data):
        #
        self.trained_estimator = return_estimator_data.get("trained_estimator")
        self.trained_data = return_estimator_data.get("estimator_data").get("trained_data")
        self.cv_data = return_estimator_data.get("estimator_data").get("cv_data")
        self.test_data = return_estimator_data.get("estimator_data").get("test_data")
        #
        if self.params_type == "default":
            self.trainingSampleCountLabel.setText(str(self.trained_data[2].shape[0]))
            self.trainingScore_1Label.setText(str(round(self.trained_data[0], 4)))
            self.trainingScore_2Label.setText(str(round(self.trained_data[1], 4)))
        else:
            self.trainingSampleCountLabel.setText(str(self.trained_data[2].shape[0]))
            self.trainingScore_1Label.setText(str(round(self.trained_data[0], 4)))
            self.trainingScore_2Label.setText(str(round(self.trained_data[1], 4)))
            # dict, list or tuple is not empty, empty is means False
            if self.cv_data:
                self.cvSampleCountLabel.setText(str(self.cv_data[2].shape[0]))
                self.cvScore_1Label.setText(str(round(self.cv_data[0], 4)))
                self.cvScore_2Label.setText(str(round(self.cv_data[1], 4)))

        # dict, list or tuple is not empty, empty is means False
        if self.test_data:
            self.testSampleCountLabel.setText(str(self.test_data[2].shape[0]))
            self.testScore_1Label.setText(str(round(self.test_data[0], 4)))
            self.testScore_2Label.setText(str(round(self.test_data[1], 4)))
        #
        best_estimator_info = "最佳模型参数:\n" + self.estimator_name + str(self.trained_estimator.get_params())
        self.bestEstimatorInfoTextBrowser.setPlainText(best_estimator_info)
        #
        self.stepLogoLabel.setPixmap(get_pixmap("finish_tip1"))
        self.stepTipLabel.setText("模型训练完成！点击按钮查询相应图表，或者点击下一步以继续操作！")
        #
        self.trainEstimatorPushButton.setEnabled(True)
        self.estimatorLearningCurveChartPushButton.setEnabled(True)
        self.estimatorEvaluationChartPushButton.setEnabled(True)
        self.previousStepPushButton.setEnabled(True)
        self.nextStepPushButton.setEnabled(True)

    def estimatorLearningCurveChartPushButtonClicked(self):
        #
        # if self.training_size is None or self.training_scores is None or self.cv_scores is None:
        self.previousStepPushButton.setEnabled(False)
        self.nextStepPushButton.setEnabled(False)
        self.estimatorLearningCurveChartPushButton.setEnabled(False)
        #
        fit_gif = get_gif("fit_model")
        self.stepLogoLabel.setPixmap(QtGui.QPixmap(""))
        self.stepLogoLabel.setMovie(fit_gif)
        fit_gif.start()
        self.stepTipLabel.setText("正在计算模型学习曲线数据,请稍后！")
        #
        self.calc_thread = RunCalcLearningCurveThread(self.trained_estimator, 
                                                    self.training_cv_samples,
                                                    self.training_params)
        self.calc_thread.update_learning_curve_data_signal.connect(self.update_learning_curve_data)
        self.calc_thread.start()
        # else:
        #     data = [self.training_size, self.training_scores, self.cv_scores]
        #     chartViewDialog = ChartViewDialog(self.qSetting, data, chart_type = "estimator_plot")
        #     chartViewDialog.exec_()

    def update_learning_curve_data(self, return_learning_curve_data):
        #
        self.training_size = return_learning_curve_data.get("training_size")
        self.training_scores = return_learning_curve_data.get("training_scores")
        self.cv_scores = return_learning_curve_data.get("cv_scores")
        #
        self.stepLogoLabel.setPixmap(get_pixmap("finish_tip1"))
        self.stepTipLabel.setText("点击按钮查询相应图表，或者点击下一步以继续操作！")
        #
        self.estimatorLearningCurveChartPushButton.setEnabled(True)
        self.estimatorEvaluationChartPushButton.setEnabled(True)
        self.previousStepPushButton.setEnabled(True)
        self.nextStepPushButton.setEnabled(True)
        #
        data = [self.training_size, self.training_scores, self.cv_scores]
        chartViewDialog = ChartViewDialog(self.qSetting, data, chart_type = "estimator_plot")
        chartViewDialog.exec_()

    def estimatorEvaluationChartPushButtonClicked(self):
        if self.test_samples is None:
            if self.params_type == "tuning":
                data = [[self.trained_data[2][:,0], self.trained_data[2][:,1], "Training", "XLabel", "YLabel"],
                        [self.cv_data[2][:, 0], self.cv_data[2][:, 1], "Corss-Validation", "XLabel", "YLabel"]]
            else:
                data = [[self.trained_data[2][:,0], self.trained_data[2][:,1], "Training", "XLabel", "YLabel"]]
        else:
            if self.params_type == "tuning":
                data = [[self.trained_data[2][:,0], self.trained_data[2][:,1], "Training", "XLabel", "YLabel"],
                        [self.cv_data[2][:, 0], self.cv_data[2][:, 1], "Corss-Validation", "XLabel", "YLabel"],
                        [self.test_data[2][:,0], self.test_data[2][:,1], "Test", "XLabel", "YLabel"]]
            else:
                data = [[self.trained_data[2][:,0], self.trained_data[2][:,1], "Training", "XLabel", "YLabel"],
                        [self.test_data[2][:,0], self.test_data[2][:,1], "Test", "XLabel", "YLabel"]]
        #
        if self.task_type == "Classification" or self.task_type == "Cluster":
            chart_type = "estimator_confusionMatrix"
        else:
            chart_type = "estimator_scatter"
        chartViewDialog = ChartViewDialog(self.qSetting, data, chart_type = chart_type)
        chartViewDialog.exec_()

    # =========================================================Save Model Data Page=========================================================

    def isSaveBestEstimatorToFileCheckBoxClicked(self):
        if not self.isSaveBestEstimatorToFileCheckBox.isChecked():
            msgResult = QMessageBox.question(self, "询问", "确定不保存训练好的模型？", QMessageBox.Yes|QMessageBox.No)
            if msgResult == QMessageBox.Yes:
                pass
            else:
                self.isSaveBestEstimatorToFileCheckBox.setChecked(True)
        
    def isSaveEstimatorDataToExcelFileNameCheckBoxClicked(self):
        #
        self.isSaveTrainingDataToWorkingSheetNameCheckBox.blockSignals(True)
        self.isSaveCVDataToWorkingSheetNameCheckBox.blockSignals(True)
        self.isSaveTestDataToWorkingSheetNameCheckBox.blockSignals(True)
        #
        if not self.isSaveEstimatorDataToExcelFileNameCheckBox.isChecked():
            self.isSaveTrainingDataToWorkingSheetNameCheckBox.setChecked(False)
            self.isSaveCVDataToWorkingSheetNameCheckBox.setChecked(False)
            self.isSaveTestDataToWorkingSheetNameCheckBox.setChecked(False)
            #
            self.isSaveTrainingDataToWorkingSheetNameCheckBox.setEnabled(False)
            self.isSaveCVDataToWorkingSheetNameCheckBox.setEnabled(False)
            self.isSaveTestDataToWorkingSheetNameCheckBox.setEnabled(False)
        else:
            self.init_saveEstimatorDataPage_UI_element()
        #
        self.isSaveTrainingDataToWorkingSheetNameCheckBox.blockSignals(False)
        self.isSaveCVDataToWorkingSheetNameCheckBox.blockSignals(False)
        self.isSaveTestDataToWorkingSheetNameCheckBox.blockSignals(False)

    def selectEstimatorDataSaveDirectoryPushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_dir =  QFileDialog.getExistingDirectory(self, "选择或创建最优模型及其数据的保存路径",
                                                     lastFileDir)
        if file_dir != "":
            self.selectEstimatorDataSaveDirectoryLineEdit.setText(file_dir)
            #
            self.qSetting.setValue("lastFileDir", file_dir)

    def resetSaveParameterPushButtonClicked(self):
        #
        self.init_saveEstimatorDataPage_UI_element()

    def saveEstimatorDataPushButtonClicked(self):
        #
        if not self.isSaveBestEstimatorToFileCheckBox.isChecked() and not self.isSaveEstimatorDataToExcelFileNameCheckBox.isChecked():
            QMessageBox.critical(self, "错误", "没有选择任何要保存到的数据？", QMessageBox.Ok)
            return
        #
        ws_name_set = []
        data_set = []
        #
        if self.isSaveBestEstimatorToFileCheckBox.isChecked():
            save_estimator_filepath = os.path.join(self.selectEstimatorDataSaveDirectoryLineEdit.text(),
                                                   self.isSaveBestEstimatorToFileLineEdit.text())
            if self.isSaveTestDataToWorkingSheetNameCheckBox.isChecked():
                estimator_info_dict = {"estimator_name":self.estimator_name,
                                    "training_samples_count":self.training_cv_samples.shape[0],
                                    "test_samples_count":self.test_samples.shape[0],
                                    "samples_features":','.join(self.training_cv_samples_features.tolist()),
                                    "cv": self.kFoldCVLineEdit.text(),
                                    "params_type": self.params_type,
                                    "trained_estimator": self.trained_estimator}
            else:
                estimator_info_dict = {"estimator_name":self.estimator_name,
                                    "training_samples_count":self.training_cv_samples.shape[0],
                                    "test_samples_count":0,
                                    "samples_features":','.join(self.training_cv_samples_features.tolist()),
                                    "cv": self.kFoldCVLineEdit.text(),
                                    "params_type": self.params_type,
                                    "trained_estimator": self.trained_estimator}
            ModelIO.save_estimator(estimator_info_dict, save_estimator_filepath)
        #
        save_data_filepath = os.path.join(self.selectEstimatorDataSaveDirectoryLineEdit.text(),
                                           self.isSaveEstimatorDataToExcelFileNameLineEdit.text())
        #
        training_data_ws_name = self.isSaveTrainingDataToWorkingSheetNameLineEdit.text()
        cv_data_ws_name = self.isSaveCVDataToWorkingSheetNameLineEdit.text()
        test_data_ws_name = self.isSaveTestDataToWorkingSheetNameLineEdit.text()
        #
        if self.isSaveTrainingDataToWorkingSheetNameCheckBox.isChecked():
            ws_name_set.append(training_data_ws_name)
            data_set.append(self.trained_data[2])
        if self.isSaveCVDataToWorkingSheetNameCheckBox.isChecked():
            ws_name_set.append(cv_data_ws_name)
            data_set.append(self.cv_data[2])
        if self.isSaveTestDataToWorkingSheetNameCheckBox.isChecked():
            ws_name_set.append(test_data_ws_name)
            data_set.append(self.test_data[2])
        #
        col_title = ["True", "Prediction"]
        ExcelIO.write_excel(save_data_filepath, ws_name_set, data_set, col_title = col_title)
        #
        QMessageBox.information(self, "提示", "最优模型及其数据已成功保存！", QMessageBox.Ok)

    # =========================================================split line=========================================================

    def previousStepPushButtonClicked(self):
        #
        i = self.scikitLearnSettingStackedWidget.currentIndex()
        if i == 1: 
            self.previousStepPushButton.setEnabled(False)
        if i == 4:
            self.cancelFinishPushButton.setIcon(get_icon("operation_cancel"))
            self.cancelFinishPushButton.setText("取消")
        #show previous page
        if i > 0:
            self.nextStepPushButton.setEnabled(True)
            stackedWidget_page_name = self.scikitLearnSettingStackedWidget.widget(i - 1).objectName()
            self.update_ui_element(stackedWidget_page_name)
            self.scikitLearnSettingStackedWidget.setCurrentIndex(i - 1)

    def nextStepPushButtonClicked(self):
        #
        i = self.scikitLearnSettingStackedWidget.currentIndex()
        if i == 0:
            self.init_selectSamplePage_UI_element()
            self.task_type = self.get_task_type()
        if i == 1: 
            if self.training_cv_samples is None:
                QMessageBox.critical(self, "错误", "未能成功读取训练-验证样本数据，请检查输入文件是否正确！", QMessageBox.Yes)
                return
            if self.test_samples is None:
                qdlg_result = QMessageBox.question(self, "询问", "“测试样本”数据输入为空，因此后续将在训练集上使用“K折交叉验证”评估模型的泛化性，是否仍继续操作？",
                                                   QMessageBox.Yes|QMessageBox.No)
                if qdlg_result == QMessageBox.No:
                    return
            self.init_setParameterPage_UI_element()
        if i == 2:
            if self.params_type == "default":
                self.kFoldCVLineEdit.setEnabled(False)
                self.nJobsComboBox.setEnabled(False)
            else:
                self.kFoldCVLineEdit.setEnabled(True)
                self.nJobsComboBox.setEnabled(True) 
            self.update_training_info()
            self.init_trainEstimatorPage_UI_element()
            self.nextStepPushButton.setEnabled(False)
        if i == 3:
            if self.params_type != "default":
                self.isSaveCVDataToWorkingSheetNameCheckBox.setEnabled(True)
                self.isSaveCVDataToWorkingSheetNameCheckBox.setChecked(True)
                self.isSaveCVDataToWorkingSheetNameLineEdit.setEnabled(True)
            if self.test_samples is not None:
                self.isSaveTestDataToWorkingSheetNameCheckBox.setEnabled(True)
                self.isSaveTestDataToWorkingSheetNameCheckBox.setChecked(True)
                self.isSaveTestDataToWorkingSheetNameLineEdit.setEnabled(True)
            #
            self.nextStepPushButton.setEnabled(False)
            self.cancelFinishPushButton.setIcon(get_icon("finish_tip2"))
            self.cancelFinishPushButton.setText("完成")
            #
            self.init_saveEstimatorDataPage_UI_element()
        #show next page
        if i < 4:
            self.scikitLearnSettingStackedWidget.setCurrentIndex(i + 1)
            stackedWidget_page_name = self.scikitLearnSettingStackedWidget.widget(i + 1).objectName()
            self.update_ui_element(stackedWidget_page_name)
            if i != 1:
                self.previousStepPushButton.setEnabled(True)

    def cancelFinishPushButtonClicked(self):
        #
        if self.scikitLearnSettingStackedWidget.currentIndex() != 4:
            qdlg_result = QMessageBox.question(self, "询问", "模型尚未训练调试完成，是否仍关闭此窗口？", QMessageBox.Yes|QMessageBox.No)
            if qdlg_result == QMessageBox.No:
                return
            else:
                self.close()
        else:
            self.close()


class RunFitEstimatorThread(QtCore.QThread):

    update_estimator_data_signal = QtCore.pyqtSignal(dict)

    def __init__(self, training_cv_samples, test_samples, 
                 task_type, estimator, params_type, 
                 basic_params, training_params):
        super().__init__()
        self.training_cv_samples = training_cv_samples
        self.test_samples = test_samples
        self.task_type = task_type
        self.estimator = estimator
        self.params_type = params_type
        self.basic_params = basic_params
        self.training_params = training_params

    def run(self):
        #
        with Manager() as process_manager:
            process_manager_return_estimator_data = process_manager.dict()
            #
            training_cv_X = self.training_cv_samples[:,:-1]
            training_cv_y = self.training_cv_samples[:,-1]
            if self.test_samples is None:
                test_X = None
                test_y = None
            else:
                test_X = self.test_samples[:,:-1]
                test_y = self.test_samples[:,-1]
            #
            estimator = ScikitLearnML(self.task_type, self.estimator, self.params_type, 
                                      self.basic_params, self.training_params)
            #
            # 下个版本须做多进程异常捕获处理
            fit_evaluate_process = Process(target = estimator.fit_validate,
                                           args = (training_cv_X, training_cv_y, test_X, test_y,
                                                   process_manager_return_estimator_data))
            fit_evaluate_process.start()
            fit_evaluate_process.join()
            #
            self.update_estimator_data_signal.emit(dict(process_manager_return_estimator_data))


class RunCalcLearningCurveThread(QtCore.QThread):

    update_learning_curve_data_signal = QtCore.pyqtSignal(dict)

    def __init__(self, trained_estimator, training_cv_samples, training_params):
        super().__init__()
        self.trained_estimator = trained_estimator
        self.training_cv_samples = training_cv_samples
        self.training_params = training_params

    def run(self):
        #
        X = self.training_cv_samples[:, :-1]
        y = self.training_cv_samples[:, -1]
        #
        n_splits = self.training_params.get("cv")
        n_jobs = self.training_params.get("n_jobs")
        #
        with Manager() as process_manager:
            process_manager_return_estimator_data = process_manager.dict()
            #
            learningCurve_process = Process(target = ScikitLearnML.learning_curve_out,
                                            args = (self.trained_estimator,
                                                    X, y, n_splits, n_jobs,
                                                    process_manager_return_estimator_data))
            #
            learningCurve_process.start()
            learningCurve_process.join()
            #
            self.update_learning_curve_data_signal.emit(dict(process_manager_return_estimator_data))

def main(setting):
    app = QApplication(sys.argv)
    scikitLearnMLDialog = ScikitLearnMLDialog(setting)
    scikitLearnMLDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

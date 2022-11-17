# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem

from ChartViewDialogDesigner import Ui_ChartViewDialog
from InitResource import get_icon
from chart.StatsChart import *

class ChartViewDialog(QDialog, Ui_ChartViewDialog):

    #
    qSetting = None
    # 

    def __init__(self, setting, data, chart_type = "plot"):
        super(ChartViewDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        #
        self.init_ui_element()
        self.connect_singal_solt()
        #
        self.data = data
        self.chart_type = chart_type
        #
        self.figures = []
        self.plot_chart()

    def init_ui_element(self):
        self.setWindowIcon(get_icon("toolBoxToolTreeWidget"))
        #
        self.selectDataFilePushButton.setIcon(get_icon("open_file"))
        self.saveChartPushButton.setIcon(get_icon("save_file"))
        self.chartSettingPushButton.setIcon(get_icon("setting"))
        #
        self.selectDataFilePushButton.setEnabled(False)
        self.chartSettingPushButton.setEnabled(False)

    def connect_singal_solt(self):
        self.saveChartPushButton.clicked.connect(self.saveChartPushButtonClicked)

    def plot_chart(self):
        #
        if self.chart_type == "estimator_plot":
            estimatorCurveChart = EstimatorCurveChart(self.data[0], self.data[1], self.data[2])
            self.chartViewHorizontalLayout.addWidget(estimatorCurveChart)
            self.figures.append(estimatorCurveChart.get_figure())
        elif self.chart_type == "estimator_scatter":
            for y_true, y_pred, title, x_label, y_label in self.data:
                estimatorScatterChart = EstimatorScatterChart(y_true, y_pred, 
                                                              title = title, 
                                                              x_label = x_label, y_label = y_label)
                self.chartViewHorizontalLayout.addWidget(estimatorScatterChart)
                self.figures.append(estimatorScatterChart.get_figure())
        elif self.chart_type == "estimator_confusionMatrix":
            for y_true, y_pred, title, x_label, y_label in self.data:
                estimatorConfusionMatrix = EstimatorConfusionMatrix(y_true, y_pred, 
                                                                    title = title, 
                                                                    x_label = x_label, y_label = y_label)
                self.chartViewHorizontalLayout.addWidget(estimatorConfusionMatrix)
                self.figures.append(estimatorConfusionMatrix.get_figure())

    def saveChartPushButtonClicked(self):
        #
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        file_path, _ =  QFileDialog.getSaveFileName(self, "创建一个保存图表的文件名",
                                                    lastFileDir,
                                                    "jpg图像(*.jpg)")
        if file_path != "":
            try:
                for i, fig in enumerate(self.figures):
                    file_path_info = os.path.splitext(file_path)
                    tmp_file_path = file_path_info[0] + '_' + str(i + 1) + file_path_info[1]
                    fig.savefig(tmp_file_path)
                #
                QMessageBox.information(self, "提示", "图表已保存至本地！")
                self.close()
            except Exception as err_info: 
                QMessageBox.critical(self, "错误", "保存图表时发生以下错误：" + str(err_info))
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(file_path))

def main(setting):
    app = QApplication(sys.argv)
    bandCalculatorDialog = ChartViewDialog(setting)
    bandCalculatorDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)





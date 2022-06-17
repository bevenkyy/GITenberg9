# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem
from fileIO import ExcelIO, ModelIO
from data.DataPreprocessor import min_max_scaler, standard_scaler

from MySQLDatabaseManagementDialogDesigner import Ui_MySQLDatabaseManagementDialog
from data.DatabaseManagement import query_database_info, MySQLDBManagement
from data import GeoserverManagement
from InitResource import get_icon

class MySQLDatabaseManagementDialog(QDialog, Ui_MySQLDatabaseManagementDialog):

    def __init__(self, setting):
        super(MySQLDatabaseManagementDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.qSetting = setting
        self.mysql_host = self.qSetting.value("mySQLHost")
        self.mysql_port = int(self.qSetting.value("mySQLPort"))
        self.user = None
        self.passwd = None
        self.mySQLDBManagement = None
        self.database_name = None
        self.table_name = None
        self.table_info = None
        #
        self.file_path_list = None
        self.curl_bin_dir = self.qSetting.value("curlBinDir")
        self.geoserver_host = self.qSetting.value("geoserverHost")
        self.geoserver_port = self.qSetting.value("geoserverPort")
        self.geoserverManagement = None
        #
        self.init_ui_element()
        self.connect_singal_solt()

    def connect_singal_solt(self):
        #========singal and slot========
       self.connectDatabasePushButton.clicked.connect( self.connectDatabasePushButtonClicked)
       self.selectDatabaseComboBox.currentIndexChanged.connect(self.selectDatabaseComboBoxCurrentIndexChanged)
       self.selectDataTableLabelComboBox.currentIndexChanged.connect(self.selectDataTableLabelComboBoxCurrentIndexChanged) 
       self.selectFilePushButton.clicked.connect(self.selectFilePushButtonClicked)
       self.delFilePushButton.clicked.connect(self.delFilePushButtonClicked)
       self.clearFilePushButton.clicked.connect(self.clearFilePushButtonClicked)

       self.loginGeoserverPushButton.clicked.connect(self.loginGeoserverPushButtonClicked)

       self.updateDatabasePublisWMSPushButton.clicked.connect(self.updateDatabasePublisWMSPushButtonClicked)

    def fill_PrimaryKey_data(self):
        #
        if self.file_path_list is not None:
            start_id = self.table_info[0][2] + 1
            for row_index in range(len(self.file_path_list)):
                self.fieldSettingTableWidget.setItem(row_index, 0, QTableWidgetItem(str(start_id)))
                start_id += 1

    def init_ui_element(self):
        #
        self.setWindowIcon(get_icon("tool_ToolBoxTreeWidget"))
        #
        self.selectFilePushButton.setIcon(get_icon("open_file"))
        self.delFilePushButton.setIcon(get_icon("del_file"))
        self.clearFilePushButton.setIcon(get_icon("clear_file"))

    def update_widget_content(self):
        #
        self.table_name = self.selectDataTableLabelComboBox.currentText()
        self.table_info = self.mySQLDBManagement.query_table_info(self.table_name)
        #
        header_labels = []
        #
        for i, field_info in enumerate(self.table_info):
            _ = QtWidgets.QTreeWidgetItem(self.dataTableInfoTreeWidget)
            header_labels.append(field_info[0])
            self.dataTableInfoTreeWidget.topLevelItem(i).setText(0, field_info[0])
            self.dataTableInfoTreeWidget.topLevelItem(i).setText(1, field_info[1])
            self.dataTableInfoTreeWidget.topLevelItem(i).setText(2, str(field_info[2]))
        #
        self.fieldSettingTableWidget.setColumnCount(len(header_labels))
        self.fieldSettingTableWidget.setHorizontalHeaderLabels(header_labels)
        if self.table_info is not None:
            self.fill_PrimaryKey_data()

    def connectDatabasePushButtonClicked(self):
        #
        try:
            self.user = self.databaseUserNameLineEdit.text()
            self.passwd = self.databaseLoginPasswordLineEdit.text()
            #
            data_base_info = query_database_info(self.mysql_host, self.mysql_port, self.user, self.passwd)
            data_base_name = data_base_info.get("database_name")
            self.selectDatabaseComboBox.addItems(data_base_name)
            QMessageBox.information(self, "提示","成功连接数据库！", QMessageBox.Ok)
            #
            self.connectDatabasePushButton.setEnabled(False)
            self.selectFilePushButton.setEnabled(True)
        except Exception as connection_info:
            QMessageBox.critical(self, "错误", "连接数据库时发生错误，错误信息如下：\n" + str(connection_info), QMessageBox.Ok)

    def selectDatabaseComboBoxCurrentIndexChanged(self):
        #
        self.selectDataTableLabelComboBox.blockSignals(True)
        #
        try:
            self.database_name = self.selectDatabaseComboBox.currentText()
            self.mySQLDBManagement = MySQLDBManagement(self.mysql_host, self.mysql_port, self.user, self.passwd, self.database_name)
            self.selectDataTableLabelComboBox.clear()
            table_list = self.mySQLDBManagement.show_datatables()
            if len(table_list) >= 1:
                self.selectDataTableLabelComboBox.addItems(table_list)
            else:
                QMessageBox.critical(self, "错误", "当前数据库中没有任何数据表！", QMessageBox.Ok)
            #
            self.update_widget_content()
        except Exception as err_info:
            QMessageBox.critical(self, "程序发生错误，错误信息如下：\n" + str(err_info), QMessageBox.Ok)
        #
        self.selectDataTableLabelComboBox.blockSignals(False)

    def loginGeoserverPushButtonClicked(self):
        #
        try:
            self.geoserverManagement = GeoserverManagement.GeoserverManagement(self.geoserver_host,
                                                                               self.geoserver_port,
                                                                               self.geoserverUserNameLineEdit.text(),
                                                                               self.geoserverLoginPasswordLineEdit.text(),
                                                                               self.curl_bin_dir)
        except Exception as err_info:
            QMessageBox.critical(self, "程序发生错误，错误信息如下：\n" + str(err_info), QMessageBox.Ok)
        #
        workspaces_name = self.geoserverManagement.get_workspace_name()
        styles_name = self.geoserverManagement.get_style_name()
        #
        self.selectWorkspaceComboBox.addItems(workspaces_name)
        self.selectRenderLayerComboBox.addItems(styles_name)

    def selectDataTableLabelComboBoxCurrentIndexChanged(self):
        #
        self.update_widget_content()

    def selectFilePushButtonClicked(self):
        lastFileDir = str(self.qSetting.value("lastFileDir"))
        if not os.path.isdir(lastFileDir):
            lastFileDir = os.path.expanduser('~')
        #
        self.file_path_list, _ =  QFileDialog.getOpenFileNames(self, "选择一个或多个影像文件",
                                                               lastFileDir,
                                                               "GeoTiff file(*.tif *.TIF);;All file(*)")
        if len(self.file_path_list) >= 1:
            #
            self.fileListWidget.addItems(self.file_path_list)
            self.fieldSettingTableWidget.setRowCount(len(self.file_path_list))
            #
            if self.table_info is not None:
                self.fill_PrimaryKey_data()
            #
            # self.delFilePushButton.setEnabled(True)
            self.clearFilePushButton.setEnabled(True)
            #
            self.qSetting.setValue("lastFileDir", os.path.dirname(self.file_path_list[0]))

    def delFilePushButtonClicked(self):
        currentIndex = self.fileListWidget.currentIndex()
        self.fileListWidget.takeItem(currentIndex.row())
    
    def clearFilePushButtonClicked(self):
        self.fileListWidget.clear()
        self.fieldSettingTableWidget.clearContents()

    def updateDatabasePublisWMSPushButtonClicked(self):
        #
        new_record_list = []
        for row_index in range(self.fieldSettingTableWidget.rowCount()):
            if self.fieldSettingTableWidget.item(row_index, 0) != None:
                tmp_record_list = []
                for col_index in range(self.fieldSettingTableWidget.columnCount()):
                    cell_object = self.fieldSettingTableWidget.item(row_index, col_index)
                    if cell_object == None:
                        tmp_record_list.append("")
                    else:
                         tmp_record_list.append(self.fieldSettingTableWidget.item(row_index, col_index).text())
                #
                new_record_list.append(tmp_record_list)
        #
        table_name = self.selectDataTableLabelComboBox.currentText()
        #
        workingspace_name = self.selectWorkspaceComboBox.currentText()
        style_name = self.selectRenderLayerComboBox.currentText()
        #
        try:
            self.mySQLDBManagement.insert_record(table_name, new_record_list)
            #
            for i, geotiff_filepath in enumerate(self.file_path_list):
                layer_name = self.fieldSettingTableWidget.item(i, 5).text()
                self.geoserverManagement.publish_geotiff(geotiff_filepath, workingspace_name, layer_name)
                self.geoserverManagement.apply_style(style_name, workingspace_name, layer_name)
            #
            QMessageBox.information(self, "提示","数据库与WMS服务更新成功！", QMessageBox.Ok)
            self.close()
        except Exception as update_info:
            QMessageBox.critical(self, "错误", "操作发生错误，错误信息如下：\n" + str(update_info), QMessageBox.Ok)

def main(setting):
    app = QApplication(sys.argv)
    mySQLDatabaseManagementDialog = MySQLDatabaseManagementDialog(setting)
    mySQLDatabaseManagementDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    setting_filename = "Setting.ini"
    qSetting = QtCore.QSettings(setting_filename, QtCore.QSettings.IniFormat)
    #
    main(qSetting)

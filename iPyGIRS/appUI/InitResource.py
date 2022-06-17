import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"python-3.7.2/Lib/site-packages"))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtGui import *

__author__ = 'SciRui'

icons_instance = None
pixmap_instance = None
gif_instance = None

def get_icon(name):
    global icons_instance
    if not icons_instance:
        icons_instance = InitResource()
    return icons_instance.icon(name)

def get_pixmap(name):
    global pixmap_instance
    if not pixmap_instance:
        pixmap_instance = InitResource()
    return pixmap_instance.pixmap(name)

def get_gif(name):
    global gif_instance
    if not gif_instance:
        gif_instance = InitResource()
    return gif_instance.gif(name)

class InitResource(object):
    def __init__(self):
        self._icons = {}
        self._pixmap = {}
        self._gif = {}
        #
        self.make_icon("appLogo", "./resource/icons/appLogo.ico")
        #
        self.make_icon("openFileToolBar", "./resource/icons/openFileToolBar.ico")
        self.make_icon("saveFileToolBar", "./resource/icons/saveFileToolBar.ico")
        self.make_icon("saveAllFileToolBar", "./resource/icons/saveAllFileToolBar.ico")
        self.make_icon("closeFileToolBar", "./resource/icons/closeFileToolBar.ico")
        self.make_icon("closeAllFileToolBar", "./resource/icons/closeAllFileToolBar.ico")
        self.make_icon("dataViewToolBar", "./resource/icons/dataViewToolBar.ico")
        self.make_icon("windowSettingToolBar", "./resource/icons/windowSettingToolBar.ico")
        self.make_icon("appSettingToolBar", "./resource/icons/appSettingToolBar.ico")
        self.make_icon("helpToolBar", "./resource/icons/helpToolBar.ico")
        self.make_icon("feedbackToolBar", "./resource/icons/feedbackToolBar.ico")
        self.make_icon("aboutToolBar", "./resource/icons/aboutToolBar.ico")
        #
        self.make_icon("tableFile_FileListTreeWidget", "./resource/icons/tableFile_FileListTreeWidget.ico")
        self.make_icon("rasterFile_FileListTreeWidget", "./resource/icons/rasterFile_FileListTreeWidget.ico")
        #
        self.make_icon("toolBox_ToolBoxTreeWidget", "./resource/icons/toolBox_ToolBoxTreeWidget.ico")
        self.make_icon("tool_ToolBoxTreeWidget", "./resource/icons/tool_ToolBoxTreeWidget.ico")
        #
        #
        self.make_icon("open_file", "./resource/icons/open_file.ico")
        self.make_icon("save_file", "./resource/icons/save_file.ico")
        self.make_icon("select_folder", "./resource/icons/select_folder.ico")     
        self.make_icon("del_file", "./resource/icons/del_file.ico")
        self.make_icon("clear_file", "./resource/icons/clear_file.ico")
        self.make_icon("load_table", "./resource/icons/load_table.ico")
        self.make_icon("setting", "./resource/icons/setting.ico")
        self.make_icon("checkError", "./resource/icons/checkError.ico")

        self.make_icon("next_step", "./resource/icons/next_step.ico")     
        self.make_icon("previous_step", "./resource/icons/previous_step.ico")
        self.make_icon("operation_cancel", "./resource/icons/operation_cancel.ico")
        self.make_icon("reset_parameter", "./resource/icons/reset_parameter.ico")
        self.make_icon("finish_tip2", "./resource/icons/finish_tip2.ico")
        self.make_icon("move_up", "./resource/icons/move_up.ico")
        self.make_icon("move_down", "./resource/icons/move_down.ico")

        self.make_icon("train_model2", "./resource/icons/train_model2.ico")
        self.make_icon("test_model", "./resource/icons/test_model.ico")

        self.make_icon("default", "./resource/icons/default.ico")

        ###pixmap###

        self.make_pixmap("import_data", "./resource/icons/import_data.ico")
        self.make_pixmap("set_parameter","./resource/icons/set_parameter.ico")
        self.make_pixmap("train_model1", "./resource/icons/train_model1.ico")
        self.make_pixmap("optimize_model","./resource/icons/optimize_model.ico")
        self.make_pixmap("export_data","./resource/icons/export_data.ico")
        self.make_pixmap("step_tip", "./resource/icons/step_tip.ico")
        self.make_pixmap("info_tip", "./resource/icons/info_tip.png")
        self.make_pixmap("finish_tip1", "./resource/icons/finish_tip1.ico")

        self.make_pixmap("default", "./resource/icons/default.ico")

        ###gif###
        self.make_gif("fit_model", "./resource/icons/fit_model.gif")

        self.make_gif("default", "./resource/icons/default.ico")
        

    def make_icon(self, name, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon


    def make_pixmap(self, name, path):
        pixmap = QPixmap(path)
        self._pixmap[name] = pixmap


    def make_gif(self, name, path):
        gif = QMovie(path)
        self._gif[name] = gif

    def icon(self, name):
        icon = self._icons["default"]
        try:
            icon = self._icons[name]
        except KeyError:
            print("icon " + name + " not found")
        return icon

    def pixmap(self, name):
        pixmap = self._pixmap["default"]
        try:
            pixmap = self._pixmap[name]
        except KeyError:
            print("icon " + name + " not found")
        return pixmap

    def gif(self, name):
        gif = self._gif["default"]
        try:
            gif = self._gif[name]
        except KeyError:
            print("icon " + name + " not found")
        return gif

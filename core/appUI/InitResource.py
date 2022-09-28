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
        resource_dir = "./core/resource/icons"
        #
        self.make_icon("appLogo", os.path.join(resource_dir, "appLogo.ico"))
        #
        self.make_icon("openFileToolBar", os.path.join(resource_dir, "openFileToolBar.ico"))
        self.make_icon("saveFileToolBar", os.path.join(resource_dir, "saveFileToolBar.ico"))
        self.make_icon("saveAllFileToolBar", os.path.join(resource_dir, "saveAllFileToolBar.ico"))
        self.make_icon("closeFileToolBar", os.path.join(resource_dir, "closeFileToolBar.ico"))
        self.make_icon("closeAllFileToolBar", os.path.join(resource_dir, "closeAllFileToolBar.ico"))
        self.make_icon("dataViewToolBar", os.path.join(resource_dir, "dataViewToolBar.ico"))
        self.make_icon("windowSettingToolBar", os.path.join(resource_dir, "windowSettingToolBar.ico"))
        self.make_icon("appSettingToolBar", os.path.join(resource_dir, "appSettingToolBar.ico"))
        self.make_icon("helpToolBar", os.path.join(resource_dir, "helpToolBar.ico"))
        self.make_icon("feedbackToolBar", os.path.join(resource_dir, "feedbackToolBar.ico"))
        self.make_icon("aboutToolBar", os.path.join(resource_dir, "aboutToolBar.ico"))
        #
        self.make_icon("tableFile_FileListTreeWidget", os.path.join(resource_dir, "tableFile_FileListTreeWidget.ico"))
        self.make_icon("rasterFile_FileListTreeWidget", os.path.join(resource_dir, "rasterFile_FileListTreeWidget.ico"))
        #
        self.make_icon("toolBox_ToolBoxTreeWidget", os.path.join(resource_dir, "toolBox_ToolBoxTreeWidget.ico"))
        self.make_icon("tool_ToolBoxTreeWidget", os.path.join(resource_dir, "tool_ToolBoxTreeWidget.ico"))
        #
        #
        self.make_icon("open_file", os.path.join(resource_dir, "open_file.ico"))
        self.make_icon("save_file", os.path.join(resource_dir, "save_file.ico"))
        self.make_icon("select_folder", os.path.join(resource_dir, "select_folder.ico")  )   
        self.make_icon("del_file", os.path.join(resource_dir, "del_file.ico"))
        self.make_icon("clear_file", os.path.join(resource_dir, "clear_file.ico"))
        self.make_icon("load_table", os.path.join(resource_dir, "load_table.ico"))
        self.make_icon("setting", os.path.join(resource_dir, "setting.ico"))
        self.make_icon("checkError", os.path.join(resource_dir, "checkError.ico"))

        self.make_icon("next_step", os.path.join(resource_dir, "next_step.ico"))     
        self.make_icon("previous_step", os.path.join(resource_dir, "previous_step.ico"))
        self.make_icon("operation_cancel", os.path.join(resource_dir, "operation_cancel.ico"))
        self.make_icon("reset_parameter", os.path.join(resource_dir, "reset_parameter.ico"))
        self.make_icon("finish_tip2", os.path.join(resource_dir, "finish_tip2.ico"))
        self.make_icon("move_up", os.path.join(resource_dir, "move_up.ico"))
        self.make_icon("move_down", os.path.join(resource_dir, "move_down.ico"))

        self.make_icon("train_model2", os.path.join(resource_dir, "train_model2.ico"))
        self.make_icon("test_model", os.path.join(resource_dir, "test_model.ico"))

        self.make_icon("default", os.path.join(resource_dir, "default.ico"))

        ###pixmap###
        self.make_pixmap("classifier_icon", os.path.join(resource_dir, "classifier_icon.png"))
        self.make_pixmap("regressor_icon",os.path.join(resource_dir, "regressor_icon.png"))
        self.make_pixmap("clusterer_icon", os.path.join(resource_dir, "clusterer_icon.png"))

        self.make_pixmap("select_task", os.path.join(resource_dir, "select_task.ico"))
        self.make_pixmap("import_data", os.path.join(resource_dir, "import_data.ico"))
        self.make_pixmap("set_parameter",os.path.join(resource_dir, "set_parameter.ico"))
        self.make_pixmap("train_model1", os.path.join(resource_dir, "train_model1.ico"))
        self.make_pixmap("optimize_model",os.path.join(resource_dir, "optimize_model.ico"))
        self.make_pixmap("export_data", os.path.join(resource_dir, "export_data.ico"))
        self.make_pixmap("step_tip", os.path.join(resource_dir, "step_tip.ico"))
        self.make_pixmap("info_tip", os.path.join(resource_dir, "info_tip.png"))
        self.make_pixmap("finish_tip1", os.path.join(resource_dir, "finish_tip1.ico"))

        self.make_pixmap("default", os.path.join(resource_dir, "default.ico"))

        ###gif###
        self.make_gif("fit_model", os.path.join(resource_dir, "fit_model.gif"))

        self.make_gif("default", os.path.join(resource_dir, "default.ico"))
        

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

# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from ScikitLearnMLDialog import ScikitLearnMLDialog
from selectMLTaskTypeDialogDesigner import Ui_selectMLTaskTypeDialog
from InitResource import get_pixmap


class SelectMLTaskTypeDialog(QDialog, Ui_selectMLTaskTypeDialog):

    def __init__(self, setting):
        super(SelectMLTaskTypeDialog, self).__init__(None)
        self.setupUi(self)
        #
        self.setting = setting
        self.init_ui_element()
        #
        #========singal and slot========
        self.connect_signal_slot()

    def init_ui_element(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        #
        self.classifierIconLabel.setPixmap(get_pixmap("classifier_icon"))
        self.classifierIconLabel.setScaledContents(True)
        self.regressorIconLabel.setPixmap(get_pixmap("regressor_icon"))
        self.regressorIconLabel.setScaledContents(True)
        self.clustererIconLabel.setPixmap(get_pixmap("clusterer_icon"))
        self.clustererIconLabel.setScaledContents(True)
        #

    def connect_signal_slot( self ):
        self.okPushButton.clicked.connect(self.okPushButtonClicked)
        self.cancelPushButton.clicked.connect(self.cancelPushButtonClicked)

    def okPushButtonClicked(self):
        task_type = ""
        if self.classifierTaskRadioButton.isChecked():
            task_type = "Classification"
        elif regressorTaskRadioButton.isChecked():
            task_type = "Regression"
        else:
            task_type = "Cluster"
        #
        self.close()
        scikitLearnMLDialog = ScikitLearnMLDialog(self.setting, task_type)
        scikitLearnMLDialog.exec()

    def cancelPushButtonClicked(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    selectMLTaskTypeDialog = SelectMLTaskTypeDialog()
    selectMLTaskTypeDialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #
    main()




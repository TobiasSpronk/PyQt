import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.UI_classes.ui_new_employee import Ui_Dialog


class NewEmployeeWindow(QtWidgets.QDialog):
    def __init__(self):
        super(NewEmployeeWindow, self).__init__()
        #app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
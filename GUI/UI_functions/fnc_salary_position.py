from PyQt5 import QtWidgets
from GUI.UI_classes.ui_salary_position import Ui_MainWindow

class EmployeeInfoWindow(QtWidgets.QMainWindow): 

    def __init__(self):
        super(EmployeeInfoWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = id
        print(self.id)

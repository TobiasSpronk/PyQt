

from PyQt5 import QtWidgets
from GUI.UI_functions.fnc_charts import ViewChartWindow
from GUI.UI_functions.fnc_manageEmployees import EmployeeManageWindow
from GUI.UI_classes.ui_mainWindow import Ui_MainWindow


class StartingPage(QtWidgets.QMainWindow):
    def __init__(self):
        # create Main Window
        super(StartingPage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # define functionallity of the buttons
        self.ui.btn_manageEmployee.clicked.connect(self.manageEmployee)
        self.ui.btn_viewCharts.clicked.connect(self.viewCharts)
    
    def manageEmployee(self):
        self.hide()
        self.employeeWindow = EmployeeManageWindow(self)
        self.employeeWindow.show() 
        
    def viewCharts(self):
        self.hide()
        self.viewChartWindow = ViewChartWindow(self)
        self.viewChartWindow.show() 

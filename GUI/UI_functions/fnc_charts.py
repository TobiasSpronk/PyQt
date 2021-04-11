
from GUI.UI_classes.ui_charts import Ui_MainWindow
#from GUI.UI_functions.fnc_mainWindow import StartingPage

from PyQt5 import QtWidgets

class ViewChartWindow(QtWidgets.QMainWindow):
    def __init__(self, mainMenu):
        super(ViewChartWindow, self).__init__()
        self.mainMenu = mainMenu
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # define button functions
        self.ui.btn_back.clicked.connect(self.back)
    
    def back(self):
        self.hide()
        self.mainMenu.show()
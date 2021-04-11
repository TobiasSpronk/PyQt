import sys
from GUI.UI_functions.fnc_mainWindow import StartingPage
from PyQt5 import QtWidgets 
from database import Database

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = StartingPage()
    mainWindow.show()
    sys.exit(app.exec_())

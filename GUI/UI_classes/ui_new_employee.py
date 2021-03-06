# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/new_employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 389)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.lbl_ID = QtWidgets.QLabel(Dialog)
        self.lbl_ID.setObjectName("lbl_ID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_ID)
        self.tf_ID = QtWidgets.QLineEdit(Dialog)
        self.tf_ID.setObjectName("tf_ID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tf_ID)
        self.lbl_FirstName = QtWidgets.QLabel(Dialog)
        self.lbl_FirstName.setObjectName("lbl_FirstName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_FirstName)
        self.tf_FirstName = QtWidgets.QLineEdit(Dialog)
        self.tf_FirstName.setObjectName("tf_FirstName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tf_FirstName)
        self.lbl_LastName = QtWidgets.QLabel(Dialog)
        self.lbl_LastName.setObjectName("lbl_LastName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_LastName)
        self.tf_LastName = QtWidgets.QLineEdit(Dialog)
        self.tf_LastName.setText("")
        self.tf_LastName.setObjectName("tf_LastName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tf_LastName)
        self.lbl_Birthday = QtWidgets.QLabel(Dialog)
        self.lbl_Birthday.setObjectName("lbl_Birthday")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lbl_Birthday)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.lbl_Position = QtWidgets.QLabel(Dialog)
        self.lbl_Position.setObjectName("lbl_Position")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_Position)
        self.tf_Position = QtWidgets.QLineEdit(Dialog)
        self.tf_Position.setText("")
        self.tf_Position.setObjectName("tf_Position")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tf_Position)
        self.lbl_Salary = QtWidgets.QLabel(Dialog)
        self.lbl_Salary.setObjectName("lbl_Salary")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl_Salary)
        self.tf_Salary = QtWidgets.QLineEdit(Dialog)
        self.tf_Salary.setText("")
        self.tf_Salary.setObjectName("tf_Salary")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tf_Salary)
        self.lbl_Department = QtWidgets.QLabel(Dialog)
        self.lbl_Department.setObjectName("lbl_Department")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lbl_Department)
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create a new Employee"))
        self.lbl_ID.setText(_translate("Dialog", "ID"))
        self.lbl_FirstName.setText(_translate("Dialog", "First Name"))
        self.lbl_LastName.setText(_translate("Dialog", "Last Name"))
        self.lbl_Birthday.setText(_translate("Dialog", "Birthday"))
        self.lbl_Position.setText(_translate("Dialog", "Position"))
        self.lbl_Salary.setText(_translate("Dialog", "Salary"))
        self.lbl_Department.setText(_translate("Dialog", "Department"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

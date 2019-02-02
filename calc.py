# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox
class Ui_Form(object):
    def addition(self):
        a=self.num1.text()
        b=self.num2.text()
        z=int(a)+int(b)
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(z))
        msg.setWindowTitle("Result")
        msg.exec()
    def subtraction(self):
        a=self.num1.text()
        b=self.num2.text()
        z=int(a)-int(b)
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(z))
        msg.setWindowTitle("Result")
        msg.exec()
    def mult(self):
        a=self.num1.text()
        b=self.num2.text()
        z=int(a)*int(b)
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(str(z))
        msg.setWindowTitle("Result")
        msg.exec()
                  
                
            
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.num1 = QtWidgets.QLineEdit(Form)
        self.num1.setGeometry(QtCore.QRect(50, 60, 113, 27))
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLineEdit(Form)
        self.num2.setGeometry(QtCore.QRect(200, 60, 113, 27))
        self.num2.setObjectName("num2")
        self.Add = QtWidgets.QPushButton(Form)
        self.Add.setGeometry(QtCore.QRect(20, 130, 99, 27))
        self.Add.setObjectName("Add")
        self.Add.clicked.connect(self.addition)
        self.sub = QtWidgets.QPushButton(Form)
        self.sub.setGeometry(QtCore.QRect(130, 130, 99, 27))
        self.sub.setObjectName("sub")
        self.sub.clicked.connect(self.subtraction)
        self.mul = QtWidgets.QPushButton(Form)
        self.mul.setGeometry(QtCore.QRect(260, 130, 99, 27))
        self.mul.setObjectName("mul")
        self.mul.clicked.connect(self.mult)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Add.setText(_translate("Form", "Add"))
        self.sub.setText(_translate("Form", "Subtract"))
        self.mul.setText(_translate("Form", "Multiply"))


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog =QtWidgets.QDialog()
    ui= Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())    

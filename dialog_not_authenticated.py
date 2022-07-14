# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_not_authenticated.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog_Not_Authenticated(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 130, 421, 181))
        self.widget.setStyleSheet("border-radius: 20px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(153, 11, 255), stop:1 rgb(255, 83, 49))")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(20, 20, 421, 191))
        self.widget_2.setStyleSheet("background-color:rgb(255, 220, 247)")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(116, 11, 145)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(370, 10, 20, 20))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color:rgb(255, 96, 43)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 110, 93, 28))
        self.pushButton_2.clicked.connect(self.next)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-radius: 10px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(153, 11, 255), stop:1 rgb(255, 83, 49));\n"
"color:rgb(255, 170, 255)")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def close(self):
        print('close')
        self.pushButton.clicked.connect(QtWidgets.qApp.quit)
        sys.exit()

    def next(self):
        print('next')
        pass

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "User has not been recognized.\n"
"Would you like to register?"))
        self.pushButton.setText(_translate("Form", "X"))
        self.pushButton_2.setText(_translate("Form", "Continue"))

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Dialog_Not_Authenticated()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

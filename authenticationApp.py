from welcome import Ui_Form
from dialog_authenticated import Ui_Dialog_Authenticated
from dialog_not_authenticated import Ui_Dialog_Not_Authenticated
from PyQt5 import QtWidgets, QtSql, uic
import sys


Ui_MainWindow, QtBaseClass = uic.loadUiType("welcome.ui")
SuccessDialogUI, LandingPageBase1 = Ui_Dialog_Authenticated, QtWidgets.QWidget
FailureDialogUI, LandingPageBase2 = Ui_Dialog_Not_Authenticated, QtWidgets.QWidget

class SuccessDialog(LandingPageBase1, SuccessDialogUI):
    def __init__(self, parent=None):
        LandingPageBase1.__init__(self, parent)
        self.setupUi(self)

class FailureDialog(LandingPageBase2, FailureDialogUI):
    def __init__(self, parent=None):   
        LandingPageBase2.__init__(self, parent)
        self.setupUi(self)

class MyApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.openDb()
        self.pushButton.clicked.connect(self.checkUser)
        
    def showSuccessForm(self):
        self.child_win = SuccessDialog(self)
        self.child_win.show()

    def showFailureForm(self):
        self.child_win = FailureDialog(self)
        self.child_win.show()

    def openDb(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.sqlite')
        if not self.db.open():
            print('Error')
        self.query = QtSql.QSqlQuery()

    def checkUser(self):
        username1 = self.lineEdit.text()
        password1 = self.lineEdit_2.text()
        print(username1, password1)
        self.query.exec_("select * from userdata where username='%s' and password='%s';" % (username1, password1))
        self.query.first()
        if self.query.value('username') != None and self.query.value('password') != None:
            print('Login succesful!')
            self.pushButton.clicked.connect(self.showSuccessForm)
        else:
            print('Login unsuccesful!')
            self.pushButton.clicked.connect(self.showFailureForm)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = MyApp()
    Form.show()
    sys.exit(app.exec_())
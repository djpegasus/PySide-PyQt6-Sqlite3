import sys
import sqlite3 as sql
from PySide6.QtWidgets import QApplication, QMainWindow
from loginUI import Ui_loginForm
from desktop import Desktop

class Crm(Ui_loginForm, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crmdb()
        
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.passRemind)
    
    def crmdb(self):
        self.conn = sql.connect("C:/Sqlite/crmdb.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("create table if not exists mfy_users(s_no INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
        self.conn.commit()

    def crmdbClose(self):
        self.conn.close()
    
    def passRemind(self):
        self.statusSet.setText("Burası Yapıulacaktır")
    
    def login(self):
        username = self.userInput.text()
        password = self.passInput.text()
        sorgu = "SELECT * FROM mfy_users where username = ? and password = ?"
        self.cursor.execute(sorgu, (username,password))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.statusSet.setText("Girilen Bilgiler Hatalıdır\nTekrar Deneyin.")
        else:
            if username == self.userInput.text() and password == self.passInput.text():
                self.statusSet.setText("Hoş Geldiniz " + username.upper())
                self.desk =Desktop()
                self.desk.show()
                self.close()
                
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    crm = Crm()
    crm.show()
    sys.exit(app.exec())
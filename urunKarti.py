import sys
import sqlite3 as sql
from PySide6.QtWidgets import QApplication, QMainWindow
from urunKartiUI import Ui_Form

class UrunKarti(Ui_Form,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crmdb()
    
    def crmdb(self):
        self.conn = sql.connect("C:/Sqlite/crmdb.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("create table if not exists urunler(s_no INTEGER PRIMARY KEY AUTOINCREMENT, urun_kodu TEXT, urun_adi TEXT, kategori TEXT, alt_kategori TEXT)")
        self.conn.commit()
    
    def crmdbClose(self):
        self.conn.close()

    def kayit(self):
        self.cursor.execute("INSERT INTO urunler ( urun_kodu, urun_adi, kategori, alt_kategori) VALUES (?,?,?,?)", 
            (self.urun_kodu.text(), self.urun_adi.text(), self.catBox.currentText(), self.subBox.currentText()))
        self.conn.commit()
        self.durumSet.setText(f"Kategori : {self.catBox.currentText()}Alt Kategor:{self.subBox.currentText()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    urun = UrunKarti()
    urun.show()
    sys.exit(app.exec())
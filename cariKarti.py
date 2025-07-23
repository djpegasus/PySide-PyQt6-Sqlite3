import sys
import sqlite3 as sql
from PySide6.QtWidgets import QApplication, QMainWindow
from cariKartiUI import Ui_Form

class CariKarti(Ui_Form,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.crmdb()
        
        self.regButton.clicked.connect(self.cariKayit)
        self.exitButton.clicked.connect(self.closeWindow)

    def crmdb(self):
        self.conn = sql.connect("C:/Sqlite/crmdb.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("create table if not exists cariler(s_no INTEGER PRIMARY KEY AUTOINCREMENT, cari_kodu TEXT, adi TEXT, sektor TEXT, doviz TEXT, vade INT, "
                            "satis_uzm TEXT, uzm_yrd TEXT, csatinalma TEXT, eposta TEXT, adres TEXT, ulke TEXT, il TEXT, ilce TEXT, muhmail TEXT, tel TEXT,mobil TEXT,fax TEXT,"
                            "v_daire TEXT, v_no TEXT, banka TEXT, iban TEXT)")
        self.conn.commit()
    
    def crmdbClose(self):
        self.conn.close()



    def cariKayit(self):
        self.cursor.execute("INSERT INTO cariler ( cari_kodu, adi, sektor, doviz, vade, satis_uzm, uzm_yrd, csatinalma, eposta,"
            "adres, ulke, il, ilce, muhmail, tel, mobil, fax, v_daire, v_no, banka, iban) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
            (self.ckodu.text(),self.cadi.text(),self.csektor.text(),self.doviz.text(),self.vade.text(),self.satisUzm.text(),self.satisYrd.text(),
            self.satinalma.text(),self.email.text(),self.addr.text(),self.ulke.text(),self.il.text(),self.ilce.text(),
            self.mmail.text(),self.tel.text(),self.mobil.text(),self.fax.text(),self.vd.text(),self.vno.text(),self.bank.text(),self.iban.text()))
        self.conn.commit()
    
    def closeWindow(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    cari = CariKarti()
    cari.show()
    sys.exit(app.exec())
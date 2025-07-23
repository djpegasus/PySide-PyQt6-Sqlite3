import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainDeskUI import Ui_mainWindow
from cariKarti import CariKarti
from urunKarti import UrunKarti



class Desktop(Ui_mainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.cariRegister.clicked.connect(self.cariReg)
        self.urunRegister.clicked.connect(self.urunReg)
        self.siparisModule.clicked.connect(self.siparis)
        self.saModule.clicked.connect(self.satinalma)
    
        
    def cariReg(self):
        self.cari =CariKarti()
        self.cari.show()
    
    def urunReg(self):
        self.urun = UrunKarti()
        self.urun.show()
    
    def siparis(self):
        pass
        
    def satinalma(self):
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    desktop = Desktop()
    desktop.show()
    sys.exit(app.exec())
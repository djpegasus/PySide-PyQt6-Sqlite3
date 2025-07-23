from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget)

class Ui_loginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(300, 200)
        self.verticalLayoutWidget = QWidget(loginForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 10, 171, 71))
        self.vbox = QVBoxLayout(self.verticalLayoutWidget)
        self.vbox.setObjectName(u"vbox")
        self.vbox.setContentsMargins(0, 0, 0, 0)

        self.userInput = QLineEdit(self.verticalLayoutWidget)
        self.userInput.setObjectName(u"userInput")
        self.vbox.addWidget(self.userInput)

        self.passInput = QLineEdit(self.verticalLayoutWidget)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.vbox.addWidget(self.passInput)

        self.verticalLayoutWidget_2 = QWidget(loginForm)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 81, 71))
        self.vbox2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.vbox2.setObjectName(u"vbox2")
        self.vbox2.setContentsMargins(0, 0, 0, 0)

        self.userLabel = QLabel(self.verticalLayoutWidget_2)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.vbox2.addWidget(self.userLabel)

        self.passLabel = QLabel(self.verticalLayoutWidget_2)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.vbox2.addWidget(self.passLabel)

        self.loginButton = QPushButton(loginForm)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(170, 110, 100, 25))

        self.registerButton = QPushButton(loginForm)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(20, 110, 125, 25))

        self.statusLabel = QLabel(loginForm)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(30, 150, 70, 20))

        self.statusSet = QLabel(loginForm)
        self.statusSet.setObjectName(u"statusSet")
        self.statusSet.setGeometry(QRect(80, 140, 190, 40))
        self.statusSet.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Form", None))
        self.userLabel.setText(QCoreApplication.translate("loginForm", u"Kullanıcı Adı", None))
        self.passLabel.setText(QCoreApplication.translate("loginForm", u"Parola", None))
        self.loginButton.setText(QCoreApplication.translate("loginForm", u"Giriş", None))
        self.registerButton.setText(QCoreApplication.translate("loginForm", u"Parolamı Unuttum", None))
        self.statusLabel.setText(QCoreApplication.translate("loginForm", u"Durum :", None))
        self.statusSet.setText("")
    # retranslateUi
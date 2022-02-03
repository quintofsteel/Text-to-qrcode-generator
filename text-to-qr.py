# quintofsteel
# qrcode generator

import pyqrcode
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 583)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(102, 102, 255);")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 791, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 201, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_image)
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(20, 140, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageLabel.setFont(font)
        self.messageLabel.setObjectName("messageLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 180, 761, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 300, 321, 271))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QRCode Generator"))
        self.label.setText(_translate("MainWindow", "Text To QRCode Generator"))
        self.pushButton.setText(_translate("MainWindow", "Generate QRCode"))
        self.messageLabel.setText(_translate("MainWindow", "Enter the message you want hidden in a QRCode: "))

    def show_image(self):
        #connecting this function to the 'Generate Button' to generate and display the qr code
        code = self.lineEdit.text()

        qr = pyqrcode.create(code)
        qr_generated = "qr-code"

        img = qr.png(qr_generated, scale = 25)  

        img = self.label_2
        img.setScaledContents(True)
        img.setPixmap(QtGui.QPixmap(qr_generated))
        img.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


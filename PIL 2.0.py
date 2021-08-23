import sys
from PIL import Image

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QTransform


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 417)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 220, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 270, 151, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 270, 151, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 211, 211))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIL 2.0"))
        self.pushButton.setText(_translate("MainWindow", "R"))
        self.pushButton_2.setText(_translate("MainWindow", "G"))
        self.pushButton_3.setText(_translate("MainWindow", "B"))
        self.pushButton_4.setText(_translate("MainWindow", "ALL"))
        self.pushButton_5.setText(_translate("MainWindow", "Против часовой стрелки"))
        self.pushButton_6.setText(_translate("MainWindow", "По часовой стрелке"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.setupUi(self)
        self.pict = Image.open(self.fname)
        self.pict.save('res.jpg')
        self.pixmap = QPixmap(self.fname)
        self.label.setPixmap(self.pixmap)
        self.position = 0
        self.pushButton.clicked.connect(self.r_channel)
        self.pushButton_2.clicked.connect(self.g_channel)
        self.pushButton_3.clicked.connect(self.b_channel)
        self.pushButton_4.clicked.connect(self.all_channel)
        self.pushButton_5.clicked.connect(self.clockwise)
        self.pushButton_6.clicked.connect(self.counterclockwise)

    def r_channel(self):
        im = Image.open('res.jpg')
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        im.save('res2.jpg')
        self.pixmap = QPixmap('res2.jpg')
        self.label.setPixmap(self.pixmap)

    def g_channel(self):
        im = Image.open('res.jpg')
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        im.save('res2.jpg')
        self.pixmap = QPixmap('res2.jpg')
        self.label.setPixmap(self.pixmap)

    def b_channel(self):
        im = Image.open('res.jpg')
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        im.save('res2.jpg')
        self.pixmap = QPixmap('res2.jpg')
        self.label.setPixmap(self.pixmap)

    def all_channel(self):
        im = Image.open('res.jpg')
        self.pixmap = QPixmap('res.jpg')
        self.label.setPixmap(self.pixmap)

    def clockwise(self):
        self.position += 90
        self.label.setPixmap(self.pixmap.transformed(QTransform().rotate(self.position)))

    def counterclockwise(self):
        self.position -= 90
        self.label.setPixmap(self.pixmap.transformed(QTransform().rotate(self.position)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
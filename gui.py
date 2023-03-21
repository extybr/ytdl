from PyQt5 import QtCore, QtGui, QtWidgets
from img import img
from decode_img_temp import decode_b64 as b64


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("main_window")
        MainWindow.resize(550, 163)
        MainWindow.setMinimumSize(QtCore.QSize(550, 163))
        MainWindow.setMaximumSize(QtCore.QSize(550, 163))
        MainWindow.setStyleSheet("background-color: rgb(108, 255, 67);")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('favicon.ico')))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.textBrowser.append(f'<img src={img}>')
        # self.textBrowser.setStyleSheet(f"background: url('favicon.ico') "
        #                                f"no-repeat center;")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(10, 120, 130, 30))
        self.pix = QtGui.QPixmap(b64()).scaled(130, 30)
        self.icon.setPixmap(self.pix)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 65, 490, 37))
        font = QtGui.QFont()
        font.setPixelSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setToolTip("example:\n"
                                 "https://www.youtube.com/watch?v=KJa5oJIaUQw&t"
                                 "\nhttps://youtu.be/KJa5oJIaUQw")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(220, 120, 101, 23))
        font = QtGui.QFont()
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        # self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(255, 0, 255);\n"
                                      "background-color: rgb(200, 255, 200);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPixelSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(170, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 130, 540, 31))
        font = QtGui.QFont()
        font.setPixelSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(360, 120, 15, 15))
        self.radioButton_1.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setToolTip('best of video. max=720p')
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(410, 120, 15, 15))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setToolTip('360p')
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(460, 120, 15, 15))
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setToolTip('144p')
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(510, 120, 15, 15))
        self.radioButton_4.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setToolTip('audio')
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("youtube downloader")
        self.pushButton.setText("download")
        self.label.setText("Paste your link")
        self.lineEdit.setText('')
        self.label_2.setText('720p   360p   144p  audio')


from sys import argv, exit
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from yt_dlp import YoutubeDL
import threading


def error(fp):
    def wrap(*args, **kwargs):
        try:
            return fp(*args, **kwargs)
        except Exception as er:
            return print(er)
    return wrap


def thread(fn):
    def execute(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return execute


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.function)

    def function(self):
        temp = str(self.ui.lineEdit.displayText())
        link = ['https://youtu.be/', 'youtu.be/', 'https://www.youtube.com/',
                'www.youtube.com/']
        if any([temp.startswith(i) for i in link]):
            self.download_video(temp)
            return self.ui.lineEdit.setText('Wait ....')
        else:
            return self.ui.lineEdit.setText('Invalid link!')

    @thread
    @error
    def download_video(self, url):
        opt = {'format': 'm4a/bestaudio/best'}
        if self.ui.radioButton_1.isChecked():
            opt = {'format': '22'}
        elif self.ui.radioButton_2.isChecked():
            opt = {'format': '18'}
        elif self.ui.radioButton_3.isChecked():
            opt = {'format': '17'}
        with YoutubeDL(opt) as ydl:
            ydl.download(url)
        self.ui.lineEdit.setText('Downloaded!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = MyWin()
    myapp.show()
    exit(app.exec_())

from sys import argv, exit
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from pytube import YouTube
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
            if [temp.startswith(i) for i in ['https://youtu.be/', 'youtu.be/']]:
                temp = temp.replace('youtu.be/', 'www.youtube.com/watch?v=')
            self.download_video(temp)
            return self.ui.lineEdit.setText('Ждите ....')
        else:
            return self.ui.lineEdit.setText('Невалидная ссылка!')

    @thread
    @error
    def download_video(self, url):
        yt = YouTube(url)
        title = ''.join(i for i in yt.title if i not in '?:/|\\') + '.mp4'
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        if self.ui.radioButton_1.isChecked():
            stream.get_highest_resolution().download('', title)
        elif self.ui.radioButton_2.isChecked():
            # stream = yt.streams.filter(progressive=True, file_extension='mp4',
            #                            resolution="360p")
            # stream.get_by_resolution("360p").download('', title)
            stream = yt.streams.get_by_itag('18')
            stream.download('', title)
        elif self.ui.radioButton_3.isChecked():
            stream = yt.streams.filter(only_audio=True).first()
            title = ''.join(i for i in yt.title if i not in '?:/|\\') + '.mp3'
            stream.download('', title)
        # self.ui.label.setText(f'Ваше видео: {yt.title} скачивается')
        self.ui.lineEdit.setText('Готово!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = MyWin()
    myapp.show()
    exit(app.exec_())

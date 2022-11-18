import sys
from random import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.btn = QPushButton('Push', self)
        self.btn.resize(100, 50)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.draw)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        self.do_paint = True
        n = randrange(10, 51)
        for i in range(n):
            qp.setBrush(QColor(randrange(128, 256), randrange(128, 256), 0))
            r = randrange(40, 101)
            qp.drawEllipse(randrange(40, 400), randrange(40, 400), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

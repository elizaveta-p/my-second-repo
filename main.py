import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from random import randint
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.w = SecondWindow()

    def run(self):
        self.w.show()
        self.w.repaint()


class SecondWindow(QWidget):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setGeometry(50, 50, 800, 800)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        r = randint(1, 400)
        qp.setBrush(QBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)), Qt.SolidPattern))
        qp.drawEllipse(randint(0, 800 - r), randint(0, 800 - r), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
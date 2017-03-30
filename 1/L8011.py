import sys
import PySide
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing")
        self.rabbit = QImage("rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([QPoint(70,100), QPoint(100,110), QPoint(130,100), QPoint(100,150)])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([QPoint(50,200), QPoint(150,200), QPoint(100,400)])

        p.drawImage(QRect(200,100,320,320), self.rabbit)
        p.end()

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing")
        self.m = QImage("2845.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,65))
        p.drawPolygon([QPoint(70,70), QPoint(100,70), QPoint(70,100)])

        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50, 150, 75, 85, 0, 155 * 16)

        p.drawPolygon([QPoint(50,150), QPoint(150,150), QPoint(150,50)])

        p.drawImage(QRect(200,100,140,140), self.m)
        p.end()

class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple drawing")
        self.m = QImage("3883.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,52,0))
        p.setBrush(QColor(0,27,42))
        p.drawPolygon([QPoint(70,100), QPoint(100,100), QPoint(100,70), QPoint(85,85), QPoint(70,70)])

        p.setPen(QColor(34,127,0))
        p.setBrush(QColor(45,127,63))
        p.drawPie(50, 150, 100, 64, 0, 180 * 16)

        p.drawPolygon([QPoint(50,200), QPoint(150,200), QPoint(125,345)])

        p.drawImage(QRect(222,55,100,100), self.m)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()
    w2 = Simple_drawing_window1()
    w2.show()
    w3 = Simple_drawing_window2()
    w3.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
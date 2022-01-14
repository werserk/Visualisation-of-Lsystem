from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
import sys
import math
from src.main_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл с данными', '', 'Текстовой файл(*.txt)')
        with open(str(file_name[0]), 'r') as file:
            self.angle, self.axiom, *theorems = file.read().split('\n')
        self.angle = float(self.angle)
        self.theorems = [i.replace('f', '0') for i in theorems]
        self.axiom.replace('f', '0')
        self.do_paint = False
        self.horizontalSlider.setTickInterval(20)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider.valueChanged.connect(self.valueChange)

    def step(self, axiom, theorems, num):
        theorems = [i.split('->') for i in theorems]
        theorems = list(filter(lambda x: x and x[0] != '', theorems))
        for i in range(num):
            for sub, to in theorems:
                axiom = axiom.replace(sub, to.lower())
            axiom = axiom.upper()
        return axiom

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_lines(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def valueChange(self, value):
        value = value // 5
        to_build = self.step(self.axiom, self.theorems, value)
        self.build(to_build)

    def draw_lines(self, qp):
        qp.setPen(QColor(255, 0, 0))
        for coords in self.coords:
            centered_coords = list(coords)
            centered_coords[0] += self.width() // 2
            centered_coords[1] += self.height() // 2
            centered_coords[2] += self.width() // 2
            centered_coords[3] += self.height() // 2
            qp.drawLine(*centered_coords)

    def build(self, to_build):
        angle_step = self.angle
        x_start = 30
        y_start = -30
        self.coords = []
        saved_steps = []
        angle = 0
        length = 10
        for char in to_build:
            if char == '+':
                angle += angle_step
                angle %= 360
            elif char == '-':
                angle -= angle_step
                angle %= 360
            elif char == '|':
                angle += 180
                angle %= 360
            elif char == '0':
                x = x_start + round(length * math.cos(angle * math.pi / 180))
                y = y_start + round(length * math.sin(angle * math.pi / 180))
                x_start = x
                y_start = y
            elif char == 'F':
                x = x_start + round(length * math.cos(angle * math.pi / 180))
                y = y_start + round(length * math.sin(angle * math.pi / 180))
                self.coords.append((x_start, y_start, x, y))
                x_start = x
                y_start = y
            elif char == '[':
                saved_steps.append([x_start, y_start, angle].copy())
            elif char == ']':
                x_start, y_start, angle = saved_steps[-1]
                del saved_steps[-1]
        self.paint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QSlider,QHBoxLayout, QLabel
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class NewWidget(QWidget):

    def __init__(self):
        super(NewWidget,self).__init__()
        self.initIU

    def initIU(self):
        sld = QSlider(Qt.Horizontal,self)
        label = QLabel(self)
        layout = QHBoxLayout()
        layout.addWidget(sld)
        layout.addWidget(label)
        self.setLayout(layout)



class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Test")
        widget= NewWidget()
        self.setCentralWidget(widget)
        self.show()

app= QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())
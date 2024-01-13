import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("Check it Off")
        self.setToolTip("Check it Off")
        self.setWindowIcon(QIcon("check_box.jpg"))
        self.initUI()

    def initUI(self):
        self.item_label = QtWidgets.QLabel(self)
        self.item_label.setText("Enter item: ")
        self.item_label.move(50, 50)

        self.item_text = QtWidgets.QLineEdit(self)
        self.item_text.move(200, 50)
        self.item_text.resize(200, 32)

        self.save_button = QtWidgets.QPushButton(self)
        self.save_button.setText("Save")
        self.save_button.clicked.connect(self.clicked)
        self.save_button.move(200, 130)

        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setText("To-do List")
        self.result_label.move(200, 170)
        self.result_label.resize(200, 200)

        self.list_label = QtWidgets.QLabel(self)
        self.list_label.setText("First item")
        self.list_label.move(200, 200)
        self.list_label.resize(200, 250)

    def clicked(self):
        self.list_label.setText("1. " + self.item_text.text())

def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec())

window()
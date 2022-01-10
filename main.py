import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.actions_group(), 0, 0)
        grid.addWidget(self.items_group(), 0, 1)
        grid.addWidget(self.text_group(), 1, 0)
        self.setLayout(grid)

        self.setWindowTitle("explorer")
        self.resize(400, 300)

    def actions_group(self):
        actions_group_title = QGroupBox("Actions")

        button_1 = QPushButton("1")
        button_2 = QPushButton("2")

        vbox = QVBoxLayout()
        vbox.addWidget(button_1)
        vbox.addWidget(button_2)
        actions_group_title.setLayout(vbox)

        return actions_group_title

    def items_group(self):
        items_group_title = QGroupBox("Items and Statistics")

        label_1 = QLabel("Lorem Ipsum")

        vbox = QVBoxLayout()
        vbox.addWidget(label_1)
        items_group_title.setLayout(vbox)

        return items_group_title

    def text_group(self):
        text_group_title = QGroupBox("Events")

        text_box = QTextEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(text_box)
        text_group_title.setLayout(vbox)

        return text_group_title


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())













# window = QWidget()
# window.resize(1920, 1080)
# layout = QVBoxLayout()
# button_1 = QPushButton("1")
# button_2 = QPushButton("2")
#
# layout.addWidget(button_1)
# layout.addWidget(button_2)
#
# def button_1_clicked():
#     alert = QMessageBox()
#     alert.setText('You clicked the button!')
#     alert.exec()
#
# button_1.clicked.connect(button_1_clicked)
#
# groupbox = QGroupBox("Example Group")
# radio = QRadioButton("Test Radio Button")
# layout.addWidget(groupbox)
# vbox = QVBoxLayout()
# vbox.addWidget(radio)
# groupbox.setLayout(vbox)
#
# window.setLayout(layout)
# window.show()
# app.exec()

from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
window.resize(1920, 1080)
layout = QVBoxLayout()
button_1 = QPushButton("1")
button_2 = QPushButton("2")

layout.addWidget(button_1)
layout.addWidget(button_2)

def button_1_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

button_1.clicked.connect(button_1_clicked)

groupbox = QGroupBox("Example Group")
radio = QRadioButton("Test Radio Button")
layout.addWidget(groupbox)
vbox = QVBoxLayout()
vbox.addWidget(radio)
groupbox.setLayout(vbox)

window.setLayout(layout)
window.show()
app.exec()

# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

button = QPushButton('Texto do botão')
button.setStyleSheet('font-size: 40px; font-weight: bold')

button2 = QPushButton('Texto do botão 2')
button2.setStyleSheet('font-size: 40px; font-weight: bold')

button3 = QPushButton('Texto do botão 2')
button3.setStyleSheet('font-size: 40px; font-weight: bold')

central_widget = QWidget()
layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(button, 1, 1, 1, 2)
layout.addWidget(button2, 4, 3, 1, 1)
layout.addWidget(button3, 7, 2, 1, 3)

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()   # O loop da aplicação

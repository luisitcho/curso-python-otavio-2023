# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)
window.setWindowTitle('Janela teste usando Python')


button1 = QPushButton('Texto do botão')
button1.setStyleSheet('font-size: 40px; font-weight: bold')

button2 = QPushButton('Texto do botão 2')
button2.setStyleSheet('font-size: 40px; font-weight: bold')

button3 = QPushButton('Texto do botão 2')
button3.setStyleSheet('font-size: 40px; font-weight: bold')


layout.addWidget(button1, 1, 1, 1, 2)
layout.addWidget(button2, 4, 3, 1, 1)
layout.addWidget(button3, 7, 2, 1, 3)


@Slot()
def slot_example(status_bar):
    def internal():
        status_bar.showMessage('Mudando a mensagem')
    return internal


@Slot()
def another_slot(checked):
    if (checked):
        print('marked')


@Slot()
def third_slot(action):
    def internal():
        another_slot(action.isChecked())

    return internal


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Status inicial')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro menu')
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Segunda ação')
second_action.setCheckable(True)
second_action.toggled.connect(another_slot)
second_action.hovered.connect(third_slot(second_action))


button2.clicked.connect(third_slot(second_action))


window.show()
app.exec()   # O loop da aplicação

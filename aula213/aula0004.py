# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (button1)
#               -> Widget 2 (button2)
#               -> Widget 3 (button3)
#   -> show
# -> exec
import sys

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


def slot_example(status_bar):
    status_bar.showMessage('Mudando a mensagem')
    print(1234)


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Status inicial')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro menu')
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(lambda: slot_example(status_bar))

layout.addWidget(button1, 1, 1, 1, 2)
layout.addWidget(button2, 4, 3, 1, 1)
layout.addWidget(button3, 7, 2, 1, 3)

window.show()
app.exec()   # O loop da aplicação

# Trabalhando com classes e herança no PySide6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Janela teste usando Python')

        # Buttons
        self.button1 = self.make_button('Texto do botão 1')
        self.button1.clicked.connect(self.slot_example)

        self.button2 = self.make_button('Texto do botão 2')

        self.button3 = self.make_button('Texto do botão 2')

        self.grid_layout.addWidget(self.button1, 1, 1, 1, 2)
        self.grid_layout.addWidget(self.button2, 4, 3, 1, 1)
        self.grid_layout.addWidget(self.button3, 7, 2, 1, 3)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Status inicial')

        # menuBar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Primeiro menu')
        self.first_action = self.first_menu.addAction('Primeira ação')
        self.first_action.triggered.connect(self.slot_example)

        self.second_action = self.first_menu.addAction('Segunda ação')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.another_slot)
        self.second_action.hovered.connect(self.another_slot)

    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('Mudando a mensagem')

    @Slot()
    def another_slot(self):
        print(f'marked? {self.second_action.isChecked()}')

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 40px; font-weight: bold')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()   # O loop da aplicação

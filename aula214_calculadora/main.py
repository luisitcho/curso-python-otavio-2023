import sys

from buttons import Button, ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON

if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Button
    # buttonsGrid.addWidget(Button('1'), 0, 0)
    # buttonsGrid.addWidget(Button('2'), 0, 1)
    # buttonsGrid.addWidget(Button('3'), 0, 2)

    # buttonsGrid.addWidget(Button('4'), 1, 1, 1, 1)

    # Executa tudo
    window.adjusteFixedSize()
    window.show()
    app.exec()

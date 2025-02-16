import sys

from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON

if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa tudo
    window.adjusteFixedSize()
    window.show()
    app.exec()

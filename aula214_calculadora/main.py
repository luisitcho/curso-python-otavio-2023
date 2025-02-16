import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    first_label = QLabel("Primeira Label")
    first_label.setStyleSheet("font-size: 100px;")

    window.v_layout.addWidget(first_label)
    window.adjusteFixedSize()

    window.show()
    app.exec()

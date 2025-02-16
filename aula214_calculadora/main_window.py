from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)

        # Título da janela
        self.setWindowTitle("Calculadora")

    # Última coisa a ser feita
    def adjusteFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

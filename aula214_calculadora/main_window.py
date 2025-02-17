from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.centralWidgetItem = QWidget()
        self.vLayout = QVBoxLayout()
        self.centralWidgetItem.setLayout(self.vLayout)
        self.setCentralWidget(self.centralWidgetItem)

        # Título da janela
        self.setWindowTitle("Calculadora")

    def adjusteFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

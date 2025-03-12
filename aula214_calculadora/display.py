from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMaximumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN] * 4)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        if isDelete:
            self.delPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        # Verifica se a tecla não tem texto
        if isEmpty(text):
            return event.ignore()

        print('texto: ', text)

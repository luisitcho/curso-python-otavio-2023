from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from utils import isEmpty, isNumOrDot
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)

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

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]

        if isEnter:
            print(f'EQ {text} pressionado, sinal emitido', type(self).__name__)
            self.eqPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        if isDelete:
            print('isDelete pressionado, sinal emitido', type(self).__name__)
            print(f'isDelete  {text}  pressionado, sinal emitido',
                  type(self).__name__)
            self.delPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        if isEsc:
            print('isEsc pressionado, sinal emitido', type(self).__name__)
            self.clearPressed.emit()
            return event.ignore()
        # return super().keyPressEvent(event)

        # Verifica se a tecla não tem texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            print('inputPressed pressionado, sinal emitido', type(self).__name__)
            self.inputPressed.emit(text)
            return event.ignore()

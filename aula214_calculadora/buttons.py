import math
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import convertToNumber, isEmpty, isNumOrDot, isValidNumber
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        # self.setCheckable(True)


class ButtonsGrid(QGridLayout):
    def __init__(
        self, display: 'Display', info: 'Info', window: 'MainWindow',
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'Del', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._operator = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, equation):
        self._equation = equation
        self.info.setText(equation)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._calculate)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOperator)

        for rowNumber, rowData in enumerate(self._gridMask):
            for columnNumber, textButton in enumerate(rowData):
                button = Button(textButton)

                if not isNumOrDot(textButton) and not isEmpty(textButton):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, columnNumber)
                slot = self._makeSlot(self._insertToDisplay, textButton)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'Del':
            self._connectButtonClicked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text in '+-/*^':
            self._connectButtonClicked(
                button, self._makeSlot(self._configLeftOperator, text)
            )
        if text == '=':
            self._connectButtonClicked(button, self._calculate)

    @Slot()  # type: ignore
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()  # type: ignore
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()  # type: ignore
    def _configLeftOperator(self, text):
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Não tem nada para colocar no valor da esquerda')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = convertToNumber(displayText)

        self._operator = text
        self.equation = f'{self._left} {self._operator} ??'

    @Slot()
    def _calculate(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Não tem nada para colocar no valor da direita')
            return

        self._right = convertToNumber(displayText)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = 'erro'

        if self._operator is None or self._left is None:
            return

        try:
            if '^' in self._operator and isinstance(self._left, (int, float)):
                result = math.pow(self._left, self._right)
                result = convertToNumber(str(result))
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Não é possível dividir por zero')
            # return
        except OverflowError:
            self._showError('Número muito extenso para ser calculado')
            # return

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'erro':
            self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _showError(self, text):
        msg = self.window.makeMessageBox()
        msg.setWindowTitle("Erro!")
        msg.setText(text)
        msg.setIcon(msg.Icon.Critical)
        self.display.setFocus()

        msg.setStandardButtons(
            msg.StandardButton.Ok | msg.StandardButton.Cancel
        )

        msg.exec()

    # def _showInfo(self, text):
    #     msg = self.window.makeMessageBox()
    #     msg.setWindowTitle("Erro!")
    #     msg.setText(text)
    #     msg.setIcon(msg.Icon.Information)

    #     msg.setStandardButtons(
    #         msg.StandardButton.Ok | msg.StandardButton.Cancel
    #     )

    #     msg.exec()

from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot, isValidNumber
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display import Display
    from info import Info


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
        self, display: 'Display', info: 'Info', *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.display = display
        self.info = info
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
        for rowNumber, rowData in enumerate(self._gridMask):
            for columnNumber, textButton in enumerate(rowData):
                button = Button(textButton)

                if not isNumOrDot(textButton) and not isEmpty(textButton):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, columnNumber)
                slot = self._makeSlot(self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*':
            self._connectButtonClicked(
                button, self._makeSlot(self._operatorClicked, button)
            )
        if text == '=':
            self._connectButtonClicked(button, self._calculate)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        textButton = button.text()
        newDisplayValue = self.display.text() + textButton

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(textButton)

    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        textButton = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            print('Não tem nada para colocar no valor da esquerda')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._operator = textButton
        self.equation = f'{self._left} {self._operator} ??'

    def _calculate(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            print('Não tem nada para colocar no valor da direita')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._operator} {self._right}'
        result = 0.0

        if self._operator is None or self._left is None:
            return

        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            print('Não é possível dividir por zero')
            return

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

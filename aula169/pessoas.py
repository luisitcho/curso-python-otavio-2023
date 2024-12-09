from contas import Conta, ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name} {attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None


if __name__ == '__main__':

    c1 = Cliente('Luis', 30)
    c1.conta = ContaCorrente(111, 222, 0, 0)

    print(c1)
    print(c1.conta)

    c2 = Cliente('Peppa', 30)
    c2.conta = ContaPoupanca(333, 444, 100)

    print(c2)
    print(c2.conta)

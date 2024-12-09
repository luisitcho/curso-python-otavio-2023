# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


# @dataclass
@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self) -> str:
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, novo_nome_completo: str) -> None:
    #     nome, *sobrenome = novo_nome_completo.split(' ')
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Luis', 'Henrique')
    # p1.nome_completo = 'Maria Helena Figueiredo'
    print(p1)
    print(p1.nome_completo)
    # p1 = Pessoa('Luis', 25)
    # p2 = Pessoa('Luis', 25)

    # print(p1 == p2)  # True
    # print(p1)  # Pessoa(nome='Luis', idade=25)

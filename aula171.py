# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass


# @dataclass
@dataclass(repr=True)
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    p1 = Pessoa('Luis', 'Henrique')
    # lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    # ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    # print(ordenadas)

    print(p1)
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])

"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


variavel = executa(saudacao, 'OI OI', 'Henrique')
print(variavel)

# Exercício - Adiando execução de funções
# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, *args):
#     def numero(n):
#         return funcao(n, *args)
#     return numero


# soma_com_cinco = criar_funcao(soma, 5)
# print(soma_com_cinco(4))
# multiplica_por_dez = criar_funcao(multiplica, 10)
# print(multiplica_por_dez(5))

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
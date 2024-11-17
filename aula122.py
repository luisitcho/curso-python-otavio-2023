# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# import sys
# sys.setrecursionlimit(10000)  # Para evitar stack overflow


# def recursiva(inicio=0, fim=4):

#     if inicio >= fim:
#         return fim

#     print(inicio, fim)
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva())

def factorial(numero):
    if numero == 1:
        return 1

    return numero * factorial(numero - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))

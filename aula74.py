# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero

    return total


multiplicacao = multiplica(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
print(multiplicacao)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):

    if numero % 2 == 0:
        return f'O numero {numero}, é par'

    return f'O numero {numero}, é impar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)

print(par_impar(1))
print(par_impar(2))
print(par_impar(3))

print(par_impar is outro_par_impar)

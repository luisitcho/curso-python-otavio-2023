# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''
Minha solução
'''

# estados = ['BA', 'SP', 'MG', 'RJ']
# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# resultado = []

# for index, cidade in enumerate(cidades):
#     resultado.append((cidade, estados[index]))

# print(resultado)

'''
Solução definitiva
'''

# def zipper(l1, l2):
#     intervalo = min(len(l1)), len(l2)
#     return [
#         (l1[i], l2[i])
#         for i in range(intervalo)
#     ]


from itertools import zip_longest
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='Sem cidade')))

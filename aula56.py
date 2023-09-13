"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luis']
lista.append('João')

# lista_enumerada = enumerate(lista)

for item in enumerate(lista):
    indice, valor = item
    print(indice, valor)

print('-'*10)

for indice, valor in enumerate(lista):
    print(indice, valor, '|', lista[indice])


print('-'*10)

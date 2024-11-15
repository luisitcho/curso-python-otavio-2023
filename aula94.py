# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# print(produto.items())

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

# print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

dc = {
    chave: valor
    for chave, valor in lista
}

# print(dict(lista))
s1 = {i * 2 for i in range(10)}
print(s1)

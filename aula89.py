# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2), = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Teste nome',
    'sobrenome': 'Teste sobrenome',
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.70
}

# print(pessoa)
# print(dados_pessoa)

dicionario = {**pessoa, 'chave': 1, **dados_pessoa}
# print(dicionario)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostra_argumentos_nomeados(*args, **kwargs):
    for chave,valor in kwargs.items():
        print(f'{chave} {valor}')


# mostra_argumentos_nomeados(peppa='Pig', teste='1 2 3')
mostra_argumentos_nomeados(**dicionario)

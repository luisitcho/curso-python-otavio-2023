# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome_completo'

pessoa[chave] = 'Luis Henrique'
pessoa['sobrenome'] = 'Teste'
print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is not None:
    print(pessoa['sobrenome'])
else:
    print('Sobrenome não existe')

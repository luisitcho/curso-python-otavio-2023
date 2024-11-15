# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Peppa',
    'sobrenome': 'Pig',
}

# print(p1['nome'])
# print(p1.get('nome', 'Nome não existe!'))

# nome = p1.pop('nome')
# print(p1)
# print(nome)

# ultima_chave = p1.popitem()
# print(p1)
# print(ultima_chave)

# p1.update({
#     'nome': 'novo valor',
#     'idade': 25,
# })

# p1.update(nome='Teste', sobrenome='teste 2')

# tupla = (('nome', 'novo valor'), ('sobrenome', 'outro valor'), ('idade', 50))
lista = [['nome', 'novo valor'], ['sobrenome', 'outro valor'], ['idade', 50]]
p1.update(lista)
print(p1)

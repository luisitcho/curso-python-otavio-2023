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
import copy

dicionario_um = {
    'chave_1': 1,
    'chave_2': 2,
    'lista_1': [0, 1, 2, 3]
}

# dicionario_dois = dicionario_um.copy()
# dicionario_dois = copy.copy(dicionario_um)
dicionario_dois = copy.deepcopy(dicionario_um)
dicionario_dois['chave_3'] = 3

dicionario_dois['lista_1'][0] = 99999999

print(dicionario_um)
print(dicionario_dois)

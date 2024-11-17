import json

# pessoa = {
#     'nome': 'Luis Henrique',
#     'sobrenome': 'Souza Cruz',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula125.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)


with open('aula125.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)

    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])

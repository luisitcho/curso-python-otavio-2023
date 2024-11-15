# groupby - agrupando valores (itertools)
from itertools import groupby
from copy import deepcopy
from pprint import pprint

# def group_by_nota(alunos):
#     return groupby(alunos, key=lambda aluno: aluno['nota'])

# # main

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    # return lambda item: item['nota']
    return aluno['nota']

alunos_agrupados = sorted(deepcopy(alunos), key=ordena)
pprint(alunos_agrupados)
print()
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    pprint(chave)
    
    for aluno in grupo:
        print(aluno)
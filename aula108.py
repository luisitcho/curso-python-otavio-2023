import copy
import pprint
from dados import produtos


def p(v):
    return pprint.pprint(v)


p(produtos)
print()
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos)
]
p(novos_produtos)
print()
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(copy.deepcopy(
    produtos), key=lambda item: item['nome'], reverse=True)
p(produtos_ordenados_por_nome)
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), key=lambda item: item['preco'])
p(produtos_ordenados_por_preco)
print()

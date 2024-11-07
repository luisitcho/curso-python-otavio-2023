import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))


lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, letra) for letra in 'Luis']
    for x in range(3)
]


p(lista)

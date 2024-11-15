"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)


soma(2, 3, 4)
soma(z=4, x=3, y=4)
soma(5, 4, 4)

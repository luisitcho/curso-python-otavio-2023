"""
Iterando strings com while
"""

nome = 'Luis Henrique'
tamanho = len(nome)
novo_nome = ''
index = 0

while index < tamanho:
    novo_nome += f'*{nome[index]}'
    index += 1

novo_nome += '*'
print(novo_nome)

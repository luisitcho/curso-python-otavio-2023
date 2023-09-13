frase = 'Todos os dias são uma oportunidade para recomeçar e para planejar um novo caminho. Siga com fé e acredite em você.'

# print(frase.count('os'))

i = 0
quantidade_letras_aparece = 0
letra_mais_aparece = ''

while i < len(frase):
    letra_atual = frase[i]
    quantidade_letras = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if quantidade_letras_aparece < quantidade_letras:
        quantidade_letras_aparece = quantidade_letras
        letra_mais_aparece = letra_atual

    i += 1

print(
    f'Letra que mais apareceu foi a "{letra_mais_aparece}", {quantidade_letras_aparece} vezes')

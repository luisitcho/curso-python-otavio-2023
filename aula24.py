# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# nome = 'Luis'
# print(nome[1])
# print(nome[-3])
# print('s' in nome)  # verifica se a letra estra entre as strings da variavel
# print('Lu' in nome)
# print(10 * '-')
# print('s' not in nome)
# print('Lu' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

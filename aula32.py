"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um numero inteiro: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O numero {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro!')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O numero {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro!')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Digite a hora em numeros inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')

#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')

#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')

#     else:
#         print('Hora invalida!')

# except:
#     print('Digite apenas números inteiros!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')

if not nome:
    print('Digite alguma coisa!')

if len(nome) > 1 and len(nome) <= 4:
    print('Seu nome é curto')

if len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')

if len(nome) > 6:
    print('Seu nome é muito grande')

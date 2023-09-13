"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Digite um numero: ')
# print(numero.isdigit())

try:
    print('string:', numero)
    numero_float = float(numero)
    print('float:', numero_float)
    print(f'O dobre de {numero} é {numero_float *2}')
except:
    print('Isso não é um numero')

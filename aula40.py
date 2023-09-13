""" Calculadora com while """

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - / *): ')

    numeros_validos = None
    operadores_permitidos = '+-/*'

    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except Exception as error:
        print(error)

    if numeros_validos is None:
        print('Um ou ambois os números não são válidos!')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    print('Realizando sua conta. COnfira o resultado abaixo:')

    if operador == '+':
        print(
            f'{numero_1_float} + {numero_2_float} = {numero_1_float + numero_2_float}')
    elif operador == '-':
        print(
            f'{numero_1_float} - {numero_2_float} = {numero_1_float - numero_2_float}')
    elif operador == '/':
        print(
            f'{numero_1_float} / {numero_2_float} = {numero_1_float / numero_2_float}')
    elif operador == '*':
        print(
            f'{numero_1_float} * {numero_2_float} = {numero_1_float * numero_2_float}')

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

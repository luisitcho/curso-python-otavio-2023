"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    opcao = input('Selecione uma opção \n[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')

        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        os.system('clear')

        try:
            apagar_valor = int(input('Escolha o indice para apagar: '))
            del lista[apagar_valor]
        except ValueError:
            print('\nDigite um número inteiro!\n')
        except IndexError:
            print('\nEste indice não existe!\n')
        except Exception:
            print('\nErro desconhecido!\n')

    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('\nNada para listar!\n')

        for indice, valor in enumerate(lista):
            print(indice, valor)
    else:
        print('\nEscolha i, a ou l\n')

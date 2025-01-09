# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)
print(argumentos)

if (qtd_argumentos <= 1):
    print('Você precisa informar pelo menos um argumento.')
else:
    try:
        print('Você passou', qtd_argumentos - 1, 'argumentos.')
        print('Os argumentos são:', ' '.join(argumentos[1:]))
    except IndexError:
        print('Erro ao imprimir argumentos.')

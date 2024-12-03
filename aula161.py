# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):

    try:

        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')

        yield arquivo

    except Exception as error:

        print('Ocorreu um erro: %s' % error)

    finally:

        print('Fechandoo arquivo')
        arquivo.close()


with my_open('aula161.txt', 'w') as arquivo:
    arquivo.write('Linha 1 - aula 161 \n')
    arquivo.write('Linha 2 - aula 161 \n')
    arquivo.write('Linha 3 - aula 161 \n', 123)
    arquivo.write('Linha 4 - aula 161 \n')
    arquivo.write('Linha 5 - aula 161 \n')
    print('WITH', arquivo)

# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/home', 'luiscruz', 'Documentos', 'Treino')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    if the_counter > 100:
        break

    print(f'{the_counter} Pasta atual {root}')

    for dir_ in dirs:
        print(f'  - Subdiretório: {dir_}')

        for file_ in files:
            caminho_completo = os.path.join(root, file_)
            print(f'    - Arquivo: {file_}')

        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)

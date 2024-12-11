# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import math
import os
from itertools import count

caminho = os.path.join('/home', 'luiscruz', 'Documentos', 'Treino')
counter = count()


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"
    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


# print(formata_tamanho(10))
# print(formata_tamanho(100))
# print(formata_tamanho(1000))
# print(formata_tamanho(10000))
# print(formata_tamanho(100000))
# print(formata_tamanho(1000000))
# print(formata_tamanho(10000000))
# print(formata_tamanho(100000000))
# print(formata_tamanho(1000000000))
# print(formata_tamanho(10000000000))
# print(formata_tamanho(100000000000))


for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    if the_counter > 100:
        break

    print(f'{the_counter} Pasta atual {root}')

    for dir_ in dirs:
        if the_counter > 10:
            break
        print(f'  - Subdiretório: {dir_}')

        for file_ in files:

            if the_counter > 10:
                break

            caminho_completo = os.path.join(root, file_)
            tamanho = os.path.getsize(caminho_completo)
            # stats = os.stat(caminho_completo)
            # tamanho = stats.st_size
            print(f'    - Arquivo: {file_} {formata_tamanho(tamanho)}')

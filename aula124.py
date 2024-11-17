import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'aula124.txt'
#
# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()
with open(caminho_arquivo, 'w+', encoding="utf-8") as arquivo:
    arquivo.write('Atenção \n')
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n')
    arquivo.writelines(('Linha 3 \n', 'Linha 4 \n'))
#     arquivo.write('Linha 1\n')  # write - escreve apenas uma linha
#     arquivo.write('Linha 2\n')

#     arquivo.writelines(  # writelines - escreve multiplas linhas, mas precisa receber um iteravel
#         ('Linha 3\n', 'Linha 4\n')
#     )

#     arquivo.seek(0, 0)  # seek - move o cursor do python pelo arquivo
#     print(arquivo.read())  # read - lê o arquivo todo

#     print('Lendo o arquivo')

#     arquivo.seek(0, 0)
#     # readline - lê linha por linha do arquivo
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline())
#     print(arquivo.readline())

#     print('Readlines - Lendo as linhas do arquivo')

#     arquivo.seek(0, 0)
#     print(arquivo.readlines())

#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('-' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

# os.remove(caminho_arquivo) # remove - apaga o arquivo
# os.unlink(caminho_arquivo) # unlink - apaga o arquivo
# os.rename(caminho_arquivo, 'aula124.txt')  # rename - renomeia o arquivo

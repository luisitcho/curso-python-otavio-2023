# os.listdir para navegar em caminhos
# /home/luiscruz/Documentos/Treino/EXEMPLO
# C:\home\luiscruz\Documentos\Treino\EXEMPLO
# caminho = r'C:\\home\\luiscruz\\Documentos\\Treino\\EXEMPLO'
import os

caminho = os.path.join('/home', 'luiscruz', 'Documentos', 'Treino')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(caminho_completo)

    print(pasta)
    if not os.path.isdir(caminho_completo):
        continue

    for item in os.listdir(caminho_completo):
        print(' ', item)

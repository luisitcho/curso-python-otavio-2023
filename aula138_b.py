from aula138_a import CAMINHO_ARQUIVO, Pessoa
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)


p1 = Pessoa(**dados[0])
p2 = Pessoa(**dados[1])
p3 = Pessoa(**dados[2])

print(p1.nome, p1.email, p1.telefone)
print(p2.nome, p2.email, p2.telefone)
print(p3.nome, p3.email, p3.telefone)

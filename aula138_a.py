# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'aula138.json'


class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone


p1 = Pessoa('João', 'joao@email.com', '(11) 98765-4321')
p2 = Pessoa('Maria', 'maria@email.com', '(21) 91234-5678')
p3 = Pessoa('Antonio', 'antonio@email.com', '(31) 92345-6789')
base_dados = [vars(p1), vars(p2), vars(p3)]

if __name__ == '__main__':
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(base_dados, arquivo, indent=4, ensure_ascii=False)

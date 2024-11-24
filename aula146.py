# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self.produtos = []

    def total(self):
        return sum(produto.preco for produto in self.produtos)

    def inserir(self, *produtos):
        for produto in produtos:
            self.produtos.append(produto)

    def listar(self):
        print()
        for produto in self.produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir(p1, p2)
print(carrinho.total())
carrinho.listar()
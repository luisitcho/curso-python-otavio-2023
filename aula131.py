# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luis'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    ...


p1 = Pessoa('Luis', 'Henrique')
# p1.nome = 'Luis'
# p1.sobrenome = 'Henrique'

print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa('Peppa', 'Pig')
# p2.nome = 'Peppa'
# p2.sobrenome = 'Pig'

print(p2.nome)
print(p2.sobrenome)

"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_boa_noite = criar_saudacao('Boa noite')
falar_bom_dia = criar_saudacao('Bom dia')

print(falar_boa_noite('Peppa'))
print(falar_bom_dia('Jackie Chan'))

print()

for nome in ['Hélio Cóptero', 'Mara Vilha', 'Giuseppe Camole']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
    print()

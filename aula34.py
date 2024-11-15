"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

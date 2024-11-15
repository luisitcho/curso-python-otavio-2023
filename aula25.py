"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

A variável variavel é definida como uma string formatada usando o operador %. 
O operador % substitui os marcadores de posição na string à esquerda pelo valor das variáveis à direita. 
O primeiro marcador de posição %s é substituído pelo valor da variável nome, 
enquanto o segundo marcador de posição %.2f é substituído pelo valor da variável preco, formatado com duas casas decimais. 
Portanto, o valor final da variável variavel será 'Luiz, o preço é R$1000.96'. 

"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (1258210, 1258210))

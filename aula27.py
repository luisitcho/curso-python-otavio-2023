"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:])  # pega as sctrings do indice passado até o fim
print(variavel[4:8])  # pega as sctrings do indice passado até o outro indice, não retorna o ultimo elemento
print(variavel[:8])  # pega as sctrings do inicio até o indice passado
print(variavel[-9: -3]) # pega os indices invertidos
print(len(variavel)) # quantidade de elementos da string
print(len(variavel[1]))
print(variavel[0:9:2]) # o passo pega de 1 em 1, ou do valor passado no terceiro parametro
print(variavel[::-1]) # inverte a ordem das strings
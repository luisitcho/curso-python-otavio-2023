"""
Introdução ao empacotamento e desempacotamento
"""

# nomes = ['Maria', 'Helena', 'Luis']
# nome1, nome2, nome3 = nomes

# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luis']
_, nome2, *_ = ['Maria', 'Helena', 'Luis']


print(nome2)
print(_)
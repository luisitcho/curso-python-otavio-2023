nome = 'Luis Henrique'
altura = 1.75
peso = 84
imc = peso / (altura * altura)

# f-strings
linha = f"{nome} e {altura:.3f}"

print(f"{nome} tem {altura} de altura, pesa {peso}KG e seu IMC é de {imc:.2f}")
print(linha)
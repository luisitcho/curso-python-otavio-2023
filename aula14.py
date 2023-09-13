a = 'A'
b = 'B'
c = 1.1
# string = 'a={} b={} c={:.2f}'  # pega a ordem das variáveis
# string = 'a={0} b={1} c={2:.2f} b={1}'  # pega a ordem dos indices
string = 'a={nome1} b={nome2} c={nome3:.2f} b={nome2} a={nome1}'  # pega pelo nome dos parametros
# formato = string.format(a, b, c)
formato = string.format(nome1=a, nome2=b, nome3=c) #parametros nomeados

print(formato)

# dir, hasattr e getattr em Python
string = 'Luis'
metodo = 'upper'

# print(dir(string))
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print(f'Não existe {metodo}')
import importlib

import aula106_m

print(aula106_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula106_m)

print('Fim')

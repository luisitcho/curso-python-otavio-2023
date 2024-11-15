# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# import sys
import aula105_m
from aula105_m import variavel_modulo, soma

# print(*sys.path, sep='\n')
# print(__name__)
print(aula105_m.variavel_modulo)
print(aula105_m.soma(1, 1))
print('-'*10)

print(variavel_modulo)
print(soma(2, 2))

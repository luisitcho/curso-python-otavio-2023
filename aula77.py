# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplica = cria_multiplicador(2)
triplica = cria_multiplicador(3)
quadruplica = cria_multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))

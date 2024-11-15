"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro = velocidade > RADAR_1
carro_nao_multado = local_carro >= (
    LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_nao_multado and velocidade_carro

if velocidade_carro:
    print('Velocidade do carro passou do radar 1')

if carro_nao_multado:
    print('Carro passou no radar 1')

if carro_multado:
    print('Carro multado no radar 1')

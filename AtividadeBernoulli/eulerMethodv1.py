import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
"""
dados do problema
g = 32.2  # aceleração da gravidade (ft/s²)
d0 = 2.5 * (1/12)  # diametro do furo na base do tanque (ft)
me = 30  # vazão mássica de entrada (lb/s)
ro = 62.4  # massa específica da água (lb/ft³)
aBase = 3  # area da base do barril (ft²)
aFuro = (np.pi * d0**2) / 4  # area do furo na base do tanque(ft²)

# resolução da EDO
    dh/dt = (me / ro * aBase) - (aFuro / aBase) * sqrt(2*g*h)
    dh/dt = f(t, h)
"""

# condição inicial t = 0; h(0) = 0
t0 = 0
h0 = 0


def f(x, y):  # f(x, y) = dy/dx
    return 0.160256 - 0.0911862 * np.sqrt(y)


numPontos = 9
deltaT = 120 / numPontos
resultado = [[t0, h0]]

i, h, t = 0, h0, t0
while i <= 120:
    h = h + deltaT * f(t, h)
    i += deltaT
    resultado.append([i, h])

# Número de pontos para a animação
nPontosf = 100
numPontos_animacao = range(1, nPontosf)  # Varie esse intervalo conforme necessário

# Função para atualizar o gráfico a cada quadro da animação
def update(frame):
    numPontos = frame + 1
    deltaT = 120 / numPontos
    resultado = [[t0, h0]]

    i, h, t = 0, h0, t0
    while i <= 120:
        h = h + deltaT * f(t, h)
        i += deltaT
        resultado.append([i, h])

    plt.cla()  # Limpar o eixo atual
    for i in range(len(resultado)):
        plt.plot(resultado[i][0], resultado[i][1], 'bo--', label='Aproximado')
    plt.title(f"Altura do líquido X Tempo [{nPontosf} pontos]")
    plt.xlabel("t [s]")
    plt.ylabel("h(t) [ft]")

# Criação da animação
fig = plt.figure(figsize=(12, 8))
animation = FuncAnimation(fig, update, frames=numPontos_animacao, interval=250, repeat=True)

animation.save(f'animação{nPontosf}pontos.gif', writer='imagemagick')

plt.show()



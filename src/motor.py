import random

from src.config import pesos, multiplicadores


def sortear_simbolo():
    acumulado = 0
    numero = random.randint(1, 100)

    for simbolo, peso in pesos.items():
        acumulado = acumulado + peso

        if numero <= acumulado:
            return simbolo


def executar_rodada():
    posicao1 = sortear_simbolo()
    posicao2 = sortear_simbolo()
    posicao3 = sortear_simbolo()

    if posicao1 == posicao2 and posicao2 == posicao3:
        multiplicador = multiplicadores[posicao1]
    else:
        multiplicador = 0

    return posicao1, posicao2, posicao3, multiplicador
from src.config import pesos, multiplicadores


def sortear_simbolo(gerador):
    acumulado = 0
    numero = gerador.randint(1, 100)

    for simbolo, peso in pesos.items():
        acumulado = acumulado + peso

        if numero <= acumulado:
            return simbolo


def executar_rodada(gerador):
    posicao1 = sortear_simbolo(gerador)
    posicao2 = sortear_simbolo(gerador)
    posicao3 = sortear_simbolo(gerador)

    if posicao1 == posicao2 and posicao2 == posicao3:
        multiplicador = multiplicadores[posicao1]
    else:
        multiplicador = 0

    return posicao1, posicao2, posicao3, multiplicador
from src.config import pesos
from src.motor import executar_rodada


def executar_simulacao(total_rodadas):
    if not isinstance(total_rodadas, int):
        raise TypeError("total_rodadas deve ser um número inteiro")

    if total_rodadas <= 0:
        raise ValueError("total_rodadas deve ser maior que zero")

    vitorias = 0

    contagem_triplas = {
        simbolo: 0
        for simbolo in pesos
    }

    contagem_simbolos = {
        simbolo: 0
        for simbolo in pesos
    }

    for rodada in range(total_rodadas):
        posicao1, posicao2, posicao3, multiplicador = executar_rodada()

        contagem_simbolos[posicao1] = contagem_simbolos[posicao1] + 1
        contagem_simbolos[posicao2] = contagem_simbolos[posicao2] + 1
        contagem_simbolos[posicao3] = contagem_simbolos[posicao3] + 1

        if multiplicador > 0:
            vitorias = vitorias + 1
            contagem_triplas[posicao1] = contagem_triplas[posicao1] + 1

    frequencia_vitorias = (vitorias / total_rodadas) * 100

    return (
        vitorias,
        frequencia_vitorias,
        contagem_triplas,
        contagem_simbolos
    )
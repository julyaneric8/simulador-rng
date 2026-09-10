from motor import executar_rodada


def executar_simulacao(total_rodadas):
    vitorias = 0

    contagem_triplas = {
        "🍒": 0,
        "🍋": 0,
        "🔔": 0,
        "💎": 0,
        "⭐": 0
    }

    contagem_simbolos = {
        "🍒": 0,
        "🍋": 0,
        "🔔": 0,
        "💎": 0,
        "⭐": 0
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
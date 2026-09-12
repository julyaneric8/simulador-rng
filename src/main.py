from src.config import pesos
from src.simulador import executar_simulacao


def main():
    seed = 42
    total_rodadas = 1000000

    (
        vitorias,
        frequencia_vitorias,
        contagem_triplas,
        contagem_simbolos
    ) = executar_simulacao(
        total_rodadas,
        seed=seed
    )

    total_simbolos = total_rodadas * 3

    print("=== RESULTADO DA SIMULAÇÃO ===")
    print()

    print("Seed:", seed)
    print("Total de rodadas:", total_rodadas)
    print("Total de símbolos:", total_simbolos)
    print("Total de vitórias:", vitorias)
    print(f"Frequência de vitórias: {frequencia_vitorias:.4f}%")

    print()
    print("=== DISTRIBUIÇÃO DOS SÍMBOLOS ===")
    print()

    for simbolo, quantidade in contagem_simbolos.items():
        porcentagem_observada = (
            quantidade / total_simbolos
        ) * 100

        porcentagem_teorica = pesos[simbolo]

        print(
            f"{simbolo} → "
            f"Quantidade: {quantidade} | "
            f"Teórico: {porcentagem_teorica:.4f}% | "
            f"Observado: {porcentagem_observada:.4f}%"
        )

    print()
    print("=== TRIPLAS: TEÓRICO X OBSERVADO ===")
    print()

    for simbolo, quantidade in contagem_triplas.items():
        probabilidade_simbolo = pesos[simbolo] / 100

        probabilidade_tripla = probabilidade_simbolo ** 3

        porcentagem_teorica_tripla = (
            probabilidade_tripla * 100
        )

        quantidade_teorica_tripla = (
            total_rodadas * probabilidade_tripla
        )

        porcentagem_observada_tripla = (
            quantidade / total_rodadas
        ) * 100

        print(
            f"{simbolo}{simbolo}{simbolo} → "
            f"Observado: {quantidade} | "
            f"Esperado: {quantidade_teorica_tripla:.2f} | "
            f"Teórico: {porcentagem_teorica_tripla:.4f}% | "
            f"Observado: {porcentagem_observada_tripla:.4f}%"
        )


if __name__ == "__main__":
    main()
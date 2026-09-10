import random

from config import pesos
from simulador import executar_simulacao


random.seed(42)


total_rodadas = 1000000

vitorias, frequencia_vitorias, contagem_triplas, contagem_simbolos = (
    executar_simulacao(total_rodadas)
)

total_simbolos = total_rodadas * 3


print("=== RESULTADO DA SIMULAÇÃO ===")
print()

print("Seed: 42")
print("Total de rodadas:", total_rodadas)
print("Total de símbolos:", total_simbolos)
print("Total de vitórias:", vitorias)
print(f"Frequência de vitórias: {frequencia_vitorias:.4f}%")


print()
print("=== DISTRIBUIÇÃO DOS SÍMBOLOS ===")
print()

for simbolo, quantidade in contagem_simbolos.items():
    porcentagem_observada = (quantidade / total_simbolos) * 100
    porcentagem_teorica = pesos[simbolo]

    print(
        f"{simbolo} → "
        f"Quantidade: {quantidade} | "
        f"Teórico: {porcentagem_teorica:.4f}% | "
        f"Observado: {porcentagem_observada:.4f}%"
    )
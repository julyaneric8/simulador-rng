warning: in the working copy of 'src/main.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/simulador.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tests/test_simulador.py', LF will be replaced by CRLF the next time Git touches it
[1mdiff --git a/src/main.py b/src/main.py[m
[1mindex 3c0793e..c5fbc59 100644[m
[1m--- a/src/main.py[m
[1m+++ b/src/main.py[m
[36m@@ -1,42 +1,47 @@[m
[31m-import random[m
[31m-[m
 from src.config import pesos[m
 from src.simulador import executar_simulacao[m
 [m
 [m
[31m-random.seed(42)[m
[31m-[m
[31m-[m
[31m-total_rodadas = 1000000[m
[32m+[m[32mdef main():[m
[32m+[m[32m    seed = 42[m
[32m+[m[32m    total_rodadas = 1000000[m
 [m
[31m-vitorias, frequencia_vitorias, contagem_triplas, contagem_simbolos = ([m
[31m-    executar_simulacao(total_rodadas)[m
[31m-)[m
[32m+[m[32m    ([m
[32m+[m[32m        vitorias,[m
[32m+[m[32m        frequencia_vitorias,[m
[32m+[m[32m        contagem_triplas,[m
[32m+[m[32m        contagem_simbolos[m
[32m+[m[32m    ) = executar_simulacao([m
[32m+[m[32m        total_rodadas,[m
[32m+[m[32m        seed=seed[m
[32m+[m[32m    )[m
 [m
[31m-total_simbolos = total_rodadas * 3[m
[32m+[m[32m    total_simbolos = total_rodadas * 3[m
 [m
[32m+[m[32m    print("=== RESULTADO DA SIMULAÇÃO ===")[m
[32m+[m[32m    print()[m
 [m
[31m-print("=== RESULTADO DA SIMULAÇÃO ===")[m
[31m-print()[m
[32m+[m[32m    print("Seed:", seed)[m
[32m+[m[32m    print("Total de rodadas:", total_rodadas)[m
[32m+[m[32m    print("Total de símbolos:", total_simbolos)[m
[32m+[m[32m    print("Total de vitórias:", vitorias)[m
[32m+[m[32m    print(f"Frequência de vitórias: {frequencia_vitorias:.4f}%")[m
 [m
[31m-print("Seed: 42")[m
[31m-print("Total de rodadas:", total_rodadas)[m
[31m-print("Total de símbolos:", total_simbolos)[m
[31m-print("Total de vitórias:", vitorias)[m
[31m-print(f"Frequência de vitórias: {frequencia_vitorias:.4f}%")[m
[32m+[m[32m    print()[m
[32m+[m[32m    print("=== DISTRIBUIÇÃO DOS SÍMBOLOS ===")[m
[32m+[m[32m    print()[m
 [m
[32m+[m[32m    for simbolo, quantidade in contagem_simbolos.items():[m
[32m+[m[32m        porcentagem_observada = (quantidade / total_simbolos) * 100[m
[32m+[m[32m        porcentagem_teorica = pesos[simbolo][m
 [m
[31m-print()[m
[31m-print("=== DISTRIBUIÇÃO DOS SÍMBOLOS ===")[m
[31m-print()[m
[32m+[m[32m        print([m
[32m+[m[32m            f"{simbolo} → "[m
[32m+[m[32m            f"Quantidade: {quantidade} | "[m
[32m+[m[32m            f"Teórico: {porcentagem_teorica:.4f}% | "[m
[32m+[m[32m            f"Observado: {porcentagem_observada:.4f}%"[m
[32m+[m[32m        )[m
 [m
[31m-for simbolo, quantidade in contagem_simbolos.items():[m
[31m-    porcentagem_observada = (quantidade / total_simbolos) * 100[m
[31m-    porcentagem_teorica = pesos[simbolo][m
 [m
[31m-    print([m
[31m-        f"{simbolo} → "[m
[31m-        f"Quantidade: {quantidade} | "[m
[31m-        f"Teórico: {porcentagem_teorica:.4f}% | "[m
[31m-        f"Observado: {porcentagem_observada:.4f}%"[m
[31m-    )[m
\ No newline at end of file[m
[32m+[m[32mif __name__ == "__main__":[m
[32m+[m[32m    main()[m
\ No newline at end of file[m
[1mdiff --git a/src/simulador.py b/src/simulador.py[m
[1mindex a67b73e..3b78be9 100644[m
[1m--- a/src/simulador.py[m
[1m+++ b/src/simulador.py[m
[36m@@ -1,14 +1,19 @@[m
[32m+[m[32mimport random[m
[32m+[m
 from src.config import pesos[m
 from src.motor import executar_rodada[m
 [m
 [m
[31m-def executar_simulacao(total_rodadas):[m
[32m+[m[32mdef executar_simulacao(total_rodadas, seed=None):[m
     if not isinstance(total_rodadas, int):[m
         raise TypeError("total_rodadas deve ser um número inteiro")[m
 [m
     if total_rodadas <= 0:[m
         raise ValueError("total_rodadas deve ser maior que zero")[m
 [m
[32m+[m[32m    if seed is not None:[m
[32m+[m[32m        random.seed(seed)[m
[32m+[m
     vitorias = 0[m
 [m
     contagem_triplas = {[m
[1mdiff --git a/tests/test_simulador.py b/tests/test_simulador.py[m
[1mindex 44ef574..f87e868 100644[m
[1m--- a/tests/test_simulador.py[m
[1m+++ b/tests/test_simulador.py[m
[36m@@ -75,6 +75,22 @@[m [mclass TestSimulador(unittest.TestCase):[m
         with self.assertRaises(TypeError):[m
             executar_simulacao(10.5)[m
 [m
[32m+[m[32m    def test_mesma_seed_deve_produzir_mesmo_resultado(self):[m
[32m+[m[32m        primeiro_resultado = executar_simulacao([m
[32m+[m[32m            100,[m
[32m+[m[32m            seed=42[m
[32m+[m[32m        )[m
[32m+[m
[32m+[m[32m        segundo_resultado = executar_simulacao([m
[32m+[m[32m            100,[m
[32m+[m[32m            seed=42[m
[32m+[m[32m        )[m
[32m+[m
[32m+[m[32m        self.assertEqual([m
[32m+[m[32m            primeiro_resultado,[m
[32m+[m[32m            segundo_resultado[m
[32m+[m[32m        )[m
[32m+[m
 [m
 if __name__ == "__main__":[m
     unittest.main()[m
\ No newline at end of file[m

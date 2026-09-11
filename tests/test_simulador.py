import sys
import unittest

sys.path.append("src")

from simulador import executar_simulacao


class TestSimulador(unittest.TestCase):

    def test_dez_rodadas_devem_contabilizar_trinta_simbolos(self):
        total_rodadas = 10

        (
            vitorias,
            frequencia_vitorias,
            contagem_triplas,
            contagem_simbolos
        ) = executar_simulacao(total_rodadas)

        total_simbolos = sum(contagem_simbolos.values())

        self.assertEqual(total_simbolos, 30)

    def test_quantidade_de_vitorias_deve_ser_valida(self):
        total_rodadas = 10

        (
            vitorias,
            frequencia_vitorias,
            contagem_triplas,
            contagem_simbolos
        ) = executar_simulacao(total_rodadas)

        self.assertGreaterEqual(vitorias, 0)
        self.assertLessEqual(vitorias, total_rodadas)

    def test_frequencia_de_vitorias_deve_ficar_entre_zero_e_cem(self):
        total_rodadas = 10

        (
            vitorias,
            frequencia_vitorias,
            contagem_triplas,
            contagem_simbolos
        ) = executar_simulacao(total_rodadas)

        self.assertGreaterEqual(frequencia_vitorias, 0)
        self.assertLessEqual(frequencia_vitorias, 100)

    def test_soma_das_triplas_deve_ser_igual_ao_total_de_vitorias(self):
        total_rodadas = 10

        (
            vitorias,
            frequencia_vitorias,
            contagem_triplas,
            contagem_simbolos
        ) = executar_simulacao(total_rodadas)

        total_triplas = sum(contagem_triplas.values())

        self.assertEqual(total_triplas, vitorias)

    def test_zero_rodadas_deve_gerar_erro(self):
        with self.assertRaises(ValueError):
            executar_simulacao(0)

    def test_numero_negativo_de_rodadas_deve_gerar_erro(self):
        with self.assertRaises(ValueError):
            executar_simulacao(-10)

    def test_texto_como_total_de_rodadas_deve_gerar_erro(self):
        with self.assertRaises(TypeError):
            executar_simulacao("dez")

    def test_numero_decimal_como_total_de_rodadas_deve_gerar_erro(self):
        with self.assertRaises(TypeError):
            executar_simulacao(10.5)


if __name__ == "__main__":
    unittest.main()
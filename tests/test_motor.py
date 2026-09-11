import unittest
from unittest.mock import patch

from src.config import pesos, multiplicadores
from src.motor import sortear_simbolo, executar_rodada


class TestMotor(unittest.TestCase):

    def test_simbolo_sorteado_deve_existir_na_configuracao(self):
        simbolo = sortear_simbolo()

        self.assertIn(simbolo, pesos)

    def test_rodada_deve_retornar_quatro_valores(self):
        resultado = executar_rodada()

        self.assertEqual(len(resultado), 4)

    def test_posicoes_devem_conter_simbolos_validos(self):
        posicao1, posicao2, posicao3, multiplicador = executar_rodada()

        self.assertIn(posicao1, pesos)
        self.assertIn(posicao2, pesos)
        self.assertIn(posicao3, pesos)

    @patch(
        "src.motor.sortear_simbolo",
        side_effect=["💎", "💎", "💎"]
    )
    def test_tripla_deve_retornar_multiplicador_correto(
        self,
        mock_sortear_simbolo
    ):
        posicao1, posicao2, posicao3, multiplicador = executar_rodada()

        self.assertEqual(posicao1, "💎")
        self.assertEqual(posicao2, "💎")
        self.assertEqual(posicao3, "💎")
        self.assertEqual(multiplicador, multiplicadores["💎"])

    @patch(
        "src.motor.sortear_simbolo",
        side_effect=["🍒", "🍋", "🔔"]
    )
    def test_simbolos_diferentes_devem_retornar_zero(
        self,
        mock_sortear_simbolo
    ):
        posicao1, posicao2, posicao3, multiplicador = executar_rodada()

        self.assertEqual(posicao1, "🍒")
        self.assertEqual(posicao2, "🍋")
        self.assertEqual(posicao3, "🔔")
        self.assertEqual(multiplicador, 0)


if __name__ == "__main__":
    unittest.main()
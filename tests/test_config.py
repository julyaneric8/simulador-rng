import unittest

from src.config import pesos


class TestConfig(unittest.TestCase):

    def test_soma_dos_pesos_deve_ser_100(self):
        soma = sum(pesos.values())

        self.assertEqual(soma, 100)


if __name__ == "__main__":
    unittest.main()
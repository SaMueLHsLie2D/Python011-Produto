import unittest
from produto import calcular_preco_com_acrescimo


class TestProduto(unittest.TestCase):
    def test_valor_valido(self):
        self.assertEqual(calcular_preco_com_acrescimo(50.00), 55.00)
        self.assertEqual(calcular_preco_com_acrescimo(100), 110.00)

    def test_valor_zero(self):
        with self.assertRaises(ValueError):
            calcular_preco_com_acrescimo(0)

    def test_valor_negativo(self):
        with self.assertRaises(ValueError):
            calcular_preco_com_acrescimo(-10)

    def test_valor_invalido(self):
        with self.assertRaises(ValueError):
            calcular_preco_com_acrescimo("abc")


if __name__ == "__main__":
    unittest.main()

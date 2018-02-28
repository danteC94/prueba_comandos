import unittest
from principal import show


class TestPrincipal(unittest.TestCase):
    def test_print(self):
        resultado = show("hola mundo")
        self.assertEqual(resultado, "hola mundo")

    def test_print(self):
        resultado = show("Bienvenido")
        self.assertEqual(resultado, "Bienvenido")


if __name__ == "__main__":
    unittest.main()

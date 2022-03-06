from procesa import procesa
import unittest


class TestCalculaMedia(unittest.TestCase):

    def test_1(self):
        resultado = procesa("s", 5, 3)
        self.assertEqual(resultado, 8)

    def test_2(self):
        resultado = procesa("r", 5, 3)
        self.assertEqual(resultado, 2)

    def test_3(self):
        resultado = procesa("d", 5, 2)
        self.assertEqual(resultado, 2.5)

    def test_4(self):
        resultado = procesa("d", 5, 0)
        self.assertEqual(resultado, None)

    def test_5(self):
        resultado = procesa("c", "Hola", "Alfredo")
        self.assertEqual(resultado, 5)

    def test_6(self):
        resultado = procesa("f", "Hola", "Alfredo")
        self.assertEqual(resultado, None)

    def test_7(self):
        resultado = procesa("s", 7)
        self.assertEqual(resultado, 8)

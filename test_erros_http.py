import unittest
from erros_http import erros_http


class TestErrosHTTP(unittest.TestCase):

    def test_codigo_401(self):
        erro = erros_http["401"]
        self.assertEqual(erro["nome"], "Unauthorized")

    def test_codigo_404(self):
        erro = erros_http["404"]
        self.assertEqual(erro["nome"], "Not Found")

    def test_codigo_inexistente(self):
        self.assertNotIn("999", erros_http)


if __name__ == "__main__":
    unittest.main()

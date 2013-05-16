import unittest

def escrevendo_no_celular(word):

    caracteres = {"ABC": "2", "DEF": "3", "GHI": "4", "JKL": "5", "MNO" : "6", "PQRS": "7", "TUV": "8", "WXYZ": "9", " ": "0"}


    for char in word:
        for chave, valor in caracteres.items():
            if char in chave:
                return valor

    return "2"

class escrevendo_no_celular_test(unittest.TestCase):
    def test_A(self):
        self.assertEquals(escrevendo_no_celular("A"), "2")

    def test_D(self):
        self.assertEquals(escrevendo_no_celular("D"), "3")

    def test_G(self):
        self.assertEquals(escrevendo_no_celular("G"), "4")

if __name__ == '__main__':
    unittest.main()
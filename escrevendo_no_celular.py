import unittest

def escrevendo_no_celular(word):

    caracteres = {"ABC": "2", "DEF": "3", "GHI": "4", "JKL": "5", "MNO" : "6", "PQRS": "7", "TUV": "8", "WXYZ": "9", " ": "0"}

    output = ""
    antiga_chave = ''
    for char in word:
        for chave, valor in caracteres.items():
            if char in chave:
                if antiga_chave == chave:
                    output += '_'

                output += valor * (chave.find(char) + 1)
                antiga_chave = chave

    return output

class escrevendo_no_celular_test(unittest.TestCase):
    def test_A(self):
        self.assertEquals(escrevendo_no_celular("A"), "2")

    def test_D(self):
        self.assertEquals(escrevendo_no_celular("D"), "3")

    def test_G(self):
        self.assertEquals(escrevendo_no_celular("G"), "4")

    def test_AD(self):
        self.assertEquals(escrevendo_no_celular("AD"), "23")

    def test_B(self):
        self.assertEquals(escrevendo_no_celular("B"), "22")

    def test_AB(self):
        self.assertEquals(escrevendo_no_celular("AB"), "2_22")

    def test_ABCA(self):
        self.assertEquals(escrevendo_no_celular("ABCA"), "2_22_222_2")


    def test_VIDALOUCA(self):
        self.assertEquals(escrevendo_no_celular("SEMPRE ACESSO O DOJOPUZZLES"), "77773367_7773302_222337777_777766606660366656667889999_9999555337777")

if __name__ == '__main__':
    unittest.main()
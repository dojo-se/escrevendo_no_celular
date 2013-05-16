import unittest

def escrevendo_no_celular(m):

    return 1

class escrevendo_no_celular_test(unittest.TestCase):
    def initial_test(self):
        self.assertEquals(escrevendo_no_celular("A"), 1)


if __name__ == '__main__':
    unittest.main()
import unittest
from MT import MT

class Testclass(unittest.TestCase):
    def test_aceitacao(self):
        mt_teste = MT()
        self.assertTrue(mt_teste.analisaPalavra('01'))
        self.assertTrue(mt_teste.analisaPalavra('011'))
        self.assertTrue(mt_teste.analisaPalavra('001'))
        self.assertTrue(mt_teste.analisaPalavra('0011'))
        self.assertTrue(mt_teste.analisaPalavra('0001'))
        self.assertTrue(mt_teste.analisaPalavra('00011'))
        self.assertTrue(mt_teste.analisaPalavra('0000011'))
        self.assertTrue(mt_teste.analisaPalavra('001111'))
        self.assertTrue(mt_teste.analisaPalavra('000011'))
        self.assertTrue(mt_teste.analisaPalavra('00111'))        
        self.assertTrue(mt_teste.analisaPalavra('000111'))
        self.assertTrue(mt_teste.analisaPalavra('011111'))
        self.assertTrue(mt_teste.analisaPalavra('0000111'))
        self.assertTrue(mt_teste.analisaPalavra('0000001'))
        self.assertTrue(mt_teste.analisaPalavra('00000111'))        
        self.assertTrue(mt_teste.analisaPalavra('00001111'))
        self.assertTrue(mt_teste.analisaPalavra('000011111'))
        self.assertTrue(mt_teste.analisaPalavra('000001111'))
        self.assertTrue(mt_teste.analisaPalavra('000000011'))
        self.assertTrue(mt_teste.analisaPalavra('0000011111'))
        self.assertTrue(mt_teste.analisaPalavra('0000001111'))
        if __name__ == "__main__":
            unittest.main()
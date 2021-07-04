import unittest

from src.venda import Dinheiro

class TestDinheiro(unittest.TestCase):
    def test_handle_value(self):
        self.assertEqual(Dinheiro.handle_value(100.554, 2, 'arredondar') , 100.55)

if __name__ == '__name__':
    unittest.main( )
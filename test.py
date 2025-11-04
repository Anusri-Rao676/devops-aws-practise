import unittest
from test import hello

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        result = hello()
        self.assertEqual(result,'hello')
if __name__ == '__main__':
    unittest.main()

import unittest
from four import greeter

class TestGreeter(unittest.TestCase):

    def test_string(self):
        self.assertTrue(greeter('Test'))

    def test_emptystring(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

if __name__ == '__main__':
    unittest.main()

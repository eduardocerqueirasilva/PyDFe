import unittest

class TestExample(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
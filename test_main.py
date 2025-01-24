# test_main.py
import unittest
from main import add1

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add1(2),3)
        self.assertEqual(add1(-1), 0)
        self.assertEqual(add1(0),1)

if __name__ == "__main__":
    unittest.main()
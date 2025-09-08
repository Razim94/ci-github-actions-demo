import unittest
from main import add   # import the function from main.py

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        # check that add(2, 3) returns 5
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()

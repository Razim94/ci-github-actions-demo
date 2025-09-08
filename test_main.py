import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main_returns_hello(self):
        self.assertEqual(main(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()

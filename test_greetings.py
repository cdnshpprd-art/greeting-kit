import unittest

from greetings import greet


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_custom_greeting(self):
        self.assertEqual(greet("Ada", "Hi"), "Hi, Ada!")


if __name__ == "__main__":
    unittest.main()

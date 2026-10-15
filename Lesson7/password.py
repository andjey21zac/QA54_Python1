import unittest


def chek_password(password):
    if len(password) < 8:
        raise ValueError("Password is too short")
    return True

class TestChekPassword(unittest.TestCase):
    def test_short_length(self):
        with self.assertRaises(ValueError):
            chek_password(password="234")
    def test_long_password(self):
        self.assertTrue(chek_password(password="Aa123456"))


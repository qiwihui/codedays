from django.test import TestCase
from utils.coding import to_bytes, to_str

class CodingTestCase(TestCase):

    def test_to_bytes(self):

        self.assertEqual(isinstance(to_bytes("it is a str"), bytes), True)
        self.assertEqual(isinstance(to_bytes(b"it is a bte"), bytes), True)

    def test_to_str(self):

        self.assertEqual(isinstance(to_str("it is a str"), str), True)
        self.assertEqual(isinstance(to_str(b"it is a bte"), str), True)

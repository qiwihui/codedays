from django.test import TestCase
from utils.coding import to_bytes, to_str

class CodingTestCase(TestCase):

    def test_to_bytes(self):

        self.assertTrue(isinstance(to_bytes("it is a str"), bytes))
        self.assertTrue(isinstance(to_bytes(b"it is a bte"), bytes))

    def test_to_str(self):

        self.assertTrue(isinstance(to_str("it is a str"), str))
        self.assertTrue(isinstance(to_str(b"it is a bte"), str))

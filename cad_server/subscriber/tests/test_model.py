from django.test import TestCase
from subscriber.models import Subscriber


# models test
class SubscriberTestCase(TestCase):

    def create_subscriber(self, email="test@test.com"):
        return Subscriber.objects.create(email=email)

    def test_subscriber_creation(self):
        w = self.create_subscriber()
        self.assertTrue(isinstance(w, Subscriber))
        self.assertEqual(w.__str__(), w.email)

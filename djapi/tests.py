from logging import currentframe
from django.test import TestCase

# Create your tests here.
from .views import Counter



class CounterTest(TestCase):

    def test_creation(self):
        """Creation works"""
        counter = Counter()
        self.assertEqual(counter.count, 0)

    def test_increment(self):
        """Increment works"""
        counter = Counter()
        incremented = counter.increment()
        self.assertEqual(incremented, 1)

    def test_increment2(self):
        """Increment works (check internal count)"""
        counter = Counter()
        counter.increment()
        incremented = counter.count
        self.assertEqual(incremented, 1)
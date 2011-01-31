"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import TestCase
from django.test.client import Client
from mytest.persons.models import Person


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}


class PersonTest(TestCase):
    def setUp(self):
        p = Person()
        p.first_name = 'Alexander'
        p.last_name = 'Tsishkovsky'
        p.skype = 'lextor_alex'
        p.save()

    def testBasic(self):
        c = Client()
        responce = c.get('/')
        self.assertEqual(responce.status_code, 200)

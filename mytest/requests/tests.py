from django.test import TestCase
from django.test.client import Client


class RequestinfoTest(TestCase):

    def testBasic(self):
        c = Client()
        responce = c.get('/reqlist/')
        self.assertEqual(responce.status_code, 200)

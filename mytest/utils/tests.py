from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class TemplateTagTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('lex', 'lex@mail.ru', '2243')
        user.save()

    def testBasic(self):
        c = Client()
        response = c.login(username='lex', password='2243')
        response = c.get('/')
        self.assertTrue('/admin/auth/user/' in response.content)

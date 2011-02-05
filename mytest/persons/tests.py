from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class PersonTest(TestCase):
    def testBasic(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)


class ContextProcTest(TestCase):
    def testBasic(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.context['settings'].TIME_ZONE, 'Ukraine/Kiev')
        self.assertNotEqual(response.content.find('django.db.backends.sqlite3'), -1)


class EditFormTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('lex', 'lex@mail.ru', '2243')
        user.save()

    def testBasic(self):
        c = Client()
        response = c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/edit/', follow=True)
        self.assertEqual(response.redirect_chain, [('http://testserver/accounts/login/?next=/edit/', 302)])
        response = c.login(username='lex', password='2243')
        self.assertTrue(response)
        response = c.get('/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.content.find('Alexander'), -1)
        response = c.post('/edit/', {'first_name': 'Newname', 'last_name': 'Newlastn', 'skype': '1'})
        response = c.get('/')
        self.assertNotEqual(response.content.find('Newname'), -1)

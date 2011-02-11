from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.template import Context, loader
from mytest.persons.models import Person


class TemplateTagTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('lex', 'lex@mail.ru', '2243')
        user.save()

    def testBasic(self):
        t = loader.get_template_from_string("{% load user_tags %}{% edit_link obj %}")
        u = User.objects.get(pk=1)
        self.assertEqual(t.render(Context({'obj': u})), '/admin/auth/user/1/')
        p = Person.objects.get(pk=1)
        self.assertEqual(t.render(Context({'obj': p})), '/admin/persons/person/1/')

from django.test import TestCase
from django.contrib.auth.models import User
from django.template import Context, loader
from mytest.persons.models import Person
from django.conf import settings
import os
import datetime
from django.db.models import get_models
from django.core.management import call_command


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


class CommandTest(TestCase):
    def testFile(self):
        os.chdir(settings.ROOT_PATH)
        os.system('./bashcommand.sh')
        self.assertEqual(os.access('%s.dat' % datetime.date.today(), os.F_OK), True)

    def testBasic(self):
        call_command('project_info', stdout=open('/dev/null', 'w'), stderr=open('%s.dat' % datetime.date.today(), 'w'))
        f = open('%s.dat' % datetime.date.today(), 'r').readlines()
        n = ["Error: [%s] - %d objects\n" % (model.__name__, model.objects.count()) for model in get_models()]
        self.assertEqual(f, n)

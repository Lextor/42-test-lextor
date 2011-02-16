from django.test import TestCase
from django.test.client import Client
from mytest.requests.models import Requestinfo, ModelEntry
from mytest.persons.models import Person
from django.conf import settings


class RequestinfoTest(TestCase):

    def testBasic(self):
        c = Client()
        responce = c.get('/reqlist/')
        self.assertEqual(responce.status_code, 200)
        r = Requestinfo.objects.get(pk=1)
        self.assertEqual(r.priority, settings.PRIORITY)


class ModelEntryTest(TestCase):
    def testBasic(self):
        pers = Person(first_name='name', last_name='lname', skype='skype')
        pers.save()

        model_entry = ModelEntry.objects.order_by('-action_time')
        self.assertEqual(model_entry[0].event, 'create')

        pers.skype = "newskype"
        pers.save()
        self.assertEqual(model_entry[0].event, 'edit')

        pers.delete()
        self.assertEqual(model_entry[0].event, 'delete')

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField(max_length=500, blank=True)
    mail_address = models.EmailField(blank=True)
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.last_name, self.first_name)

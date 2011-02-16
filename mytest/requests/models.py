from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import Message
from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from django.conf import settings


class Requestinfo(models.Model):
    time = models.DateTimeField(auto_now=True)
    path_info = models.CharField(max_length=255)
    request_method = models.CharField(max_length=5)
    http_user_agent = models.CharField(max_length=255)
    lang = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)
    priority = models.IntegerField(default=settings.PRIORITY)


EVENT_CHOICES = {
    True: 'create',
    False: 'edit',
    None: 'delete'}


class ModelEntry(models.Model):
    action_time = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.IntegerField()
    event = models.CharField(max_length=6, choices=(('create', 'Create'),
                                                    ('edit', 'Edit'), ('delete', 'Delete')))


def event(sender, instance, **kwargs):
    if sender not in (ModelEntry, Requestinfo, Message, Session, LogEntry):
        ModelEntry.objects.create(content_type=ContentType.objects.get_for_model(sender),
                                  object_id=instance.id, event=EVENT_CHOICES[kwargs.get('created')])


post_save.connect(event)
post_delete.connect(event)

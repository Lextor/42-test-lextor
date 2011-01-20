from django.db import models


class Requestlist(models.Model):
    time = models.DateTimeField(auto_now=True)
    path_info = models.CharField(max_length=256)
    request_method = models.CharField(max_length=5)
    http_user_agent = models.CharField(max_length=256)
    lang = models.CharField(max_length=50)
    tz = models.CharField(max_length=50)

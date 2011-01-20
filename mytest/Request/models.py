from django.db import models

class Requestlist(models.Model):
    path_info = models.CharField(max_length=100)
    request_method = models.CharField(max_length=10)
    http_user_agent = models.TextField(max_length=500)
    log_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=30)

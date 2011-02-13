from django.contrib import admin
from mytest.requests.models import ModelEntry


class ModelEntryAdmin(admin.ModelAdmin):
        list_display = ('content_type', 'object_id', 'action_time', 'event')

admin.site.register(ModelEntry, ModelEntryAdmin)

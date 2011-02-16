from django.contrib import admin
from mytest.requests.models import Requestinfo, ModelEntry


def increase(modeladmin, request, queryset):
    queryset.update(priority=1)
increase.short_description = "Increase requests priority"


def decrease(modeladmin, request, queryset):
    queryset.update(priority=0)
decrease.short_description = "Decrease requests priority"


class RequestinfoAdmin(admin.ModelAdmin):
        list_display = ('id', 'time', 'priority')
        actions = [increase, decrease]


class ModelEntryAdmin(admin.ModelAdmin):
        list_display = ('content_type', 'object_id', 'action_time', 'event')

admin.site.register(ModelEntry, ModelEntryAdmin)
admin.site.register(Requestinfo, RequestinfoAdmin)

from django.contrib import admin
from mytest.persons.models import Person


class PersonAdmin(admin.ModelAdmin):
        list_display = ('id', 'last_name', 'first_name', 'date_of_birth')

admin.site.register(Person, PersonAdmin)

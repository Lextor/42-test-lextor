from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mytest.persons.models import Person
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson
from django.forms.widgets import TextInput
from django.conf import settings
from django import forms


class CalendarWidget(TextInput):
    class Media:
        js = (settings.MEDIA_URL + "js/jquery-ui/js/jquery-1.4.4.min.js",
              settings.MEDIA_URL + "js/jquery-ui/js/jquery-ui-1.8.9.custom.min.js",
              settings.MEDIA_URL + "js/jquery-ui/development-bundle/ui/i18n/jquery-ui-i18n.js")
        css = {"all": (settings.MEDIA_URL + "js/jquery-ui/css/ui-lightness/jquery-ui-1.8.9.custom.css",)}


class PersonForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=CalendarWidget)

    class Meta:
        model = Person

    class Media:
        js = (settings.MEDIA_URL + "js/jquery-ui/js/jquery-1.4.4.min.js",
              settings.MEDIA_URL + "js/jquery-ui/js/jquery.form.js",
              settings.MEDIA_URL + "js/jquery-ui/js/jquery.blockUI.js")


@login_required
def edit_personinfo(request):
    if request.is_ajax() and request.method == 'POST':
        form = PersonForm(request.POST, instance=Person.objects.get(pk=1))
        if form.is_valid():
            form.save()
            status = 'ok'
            message = 'Person info updated'
        else:
            status = 'error'
            message = ''
        response_text = render_to_string("edit_personinfo_form.html", {'form': form})
        return HttpResponse(simplejson.dumps({'status': status, 'text': response_text, 'message': message}), mimetype='application/javascript')
    else:
        form = PersonForm(instance=Person.objects.get(pk=1))
    return render_to_response("edit_personinfo.html", RequestContext(request, {'form': form}))

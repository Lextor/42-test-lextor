from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mytest.persons.models import Person
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson


class PersonForm(ModelForm):
    class Meta:
        model = Person


@login_required
def edit_personinfo(request):
    if request.is_ajax() and request.method == 'POST':
        form = PersonForm(request.POST, instance=Person.objects.get(pk=1))
        if form.is_valid():
            form.save()
            status = 'ok'
        else:
            status = 'error'
        response_text = render_to_string("edit_personinfo_form.html", {'form': form})
        return HttpResponse(simplejson.dumps({'status': status, 'text': response_text}), mimetype='application/javascript')
    else:
        form = PersonForm(instance=Person.objects.get(pk=1))
    return render_to_response("edit_personinfo.html", RequestContext(request, {'form': form}))

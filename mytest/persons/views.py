from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mytest.persons.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person


@login_required
def edit_personinfo(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=Person.objects.get(pk=1))
        if form.is_valid():
            form.save()
    else:
        form = PersonForm(instance=Person.objects.get(pk=1))
    return render_to_response("edit_personinfo.html", RequestContext(request, {'form': form}))

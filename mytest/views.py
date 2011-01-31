from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from mytest.persons.models import Person



def index(request):
    person = get_object_or_404(Person, id=1)
    return render_to_response("main.html", RequestContext(request, {"person": person}))

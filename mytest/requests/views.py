from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from mytest.requests.models import Requestinfo


def request_list(request):
    requestlist = Requestinfo.objects.all().order_by('-id')[:10]
    return render_to_response("request.html", RequestContext(request, {"requestlist": requestlist}))

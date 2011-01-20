from django.conf import settings
from mytest.Request.models import Requestlist


class RequestlistMiddleware(object):
    def process_request(self, request):
        inst = Requestlist()
        inst.path_info = request.META['PATH_INFO']
        inst.request_method = request.META['REQUEST_METHOD']
        inst.http_user_agent = request.META['HTTP_USER_AGENT']
        inst.lang = request.META['LANG']
        inst.tz = request.META['TZ']
        inst.save()

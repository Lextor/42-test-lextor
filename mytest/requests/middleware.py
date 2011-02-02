from models import Requestinfo


class RequestinfoMiddleware(object):
    def process_request(self, request):
        inst = Requestinfo()
        inst.path_info = request.META['PATH_INFO'][:255]
        inst.request_method = request.META['REQUEST_METHOD']
        inst.http_user_agent = request.META.get('HTTP_USER_AGENT', '')[:255]
        inst.lang = request.META.get('LANG', '')
        inst.tz = request.META.get('TZ', '')
        inst.save()

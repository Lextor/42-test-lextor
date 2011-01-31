from models import Requestinfo


class RequestinfoMiddleware(object):
    def process_request(self, request):
        inst = Requestinfo()
        inst.path_info = request.META['PATH_INFO']
        inst.request_method = request.META['REQUEST_METHOD']

        if 'HTTP_USER_AGENT' in request.META:
            inst.http_user_agent = request.META['HTTP_USER_AGENT']
        else:
            inst.http_user_agent = ''

        if 'LANG' in request.META:
            inst.lang = request.META['LANG']
        else:
            inst.lang = ''

        if 'TZ' in request.META:
            inst.tz = request.META['TZ']
        else:
            inst.tz = ''

        inst.save()

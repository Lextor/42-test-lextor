from django.conf.urls.defaults import *


urlpatterns = patterns('mytest.requests.views',
    url(r'^$', 'request_list', name='request-list'),
)

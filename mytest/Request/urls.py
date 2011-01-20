from django.conf.urls.defaults import *


urlpatterns = patterns('mytest.Request.views',
    url(r'^$', 'request_list', name='request_list'),
)

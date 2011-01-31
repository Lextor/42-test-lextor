from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'mytest.views.index'),
    (r'^reqlist/$', include('mytest.requests.urls')),
    (r'^admin/', include(admin.site.urls)),
)

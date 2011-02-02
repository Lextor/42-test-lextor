from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'mytest.views.index'),
    (r'^reqlist/$', include('mytest.requests.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='auth_login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
)

from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mytest.views.index', name='index'),
    (r'^reqlist/$', include('mytest.requests.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    (r'^edit/$', 'mytest.persons.views.edit_personinfo'),
)

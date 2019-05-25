from django.conf.urls import patterns, include, urls
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$'), 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blod.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^hello', 'helloworld.views.index'),
    
)

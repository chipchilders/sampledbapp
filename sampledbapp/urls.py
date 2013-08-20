from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from hello import index

urlpatterns = patterns('',
    url(r'^sampledbapp/index', index, name='index'),
    url(r'^sampledbapp/', index, name='index'),
    url(r'^$', index, name='index'),
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^sampleapp/', include('sampleapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

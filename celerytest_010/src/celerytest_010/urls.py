from django.conf.urls import patterns, include, url
from demo import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'celerytest_010.views.home', name='home'),
    # url(r'^celerytest_010/', include('celerytest_010.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^show/$', views.show),
)

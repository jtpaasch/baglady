from django.conf.urls import patterns, include, url

# Use django's built-in admin.
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Enable django's built-in admin URLs.
    url(r'^admin/', include(admin.site.urls)),
)

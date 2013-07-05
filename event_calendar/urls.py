from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'event_calendar.views.home', name='home'),
    # url(r'^event_calendar/', include('event_calendar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^', include('events.urls')),    
    url(r'^$', 'events.views.index'),
    url(r'^calendar/', include('events.urls')),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
)

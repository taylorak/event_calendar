'''
Created on Jun 17, 2013

@author: taylorak
'''

from django.conf.urls import patterns, url
#from django.views.generic import ListView, DetailView
#from events.models import event, announcement 

urlpatterns = patterns('',
    url(r'^$', 'events.views.index'),
    url(r'^(?P<year>d{4})/(?P<month>d{2})/(?P<day>d{2})/$','events.views.day'),
    url(r'^(?P<year>d{4})/(?P<month>d{2})/$','events.views.month'),
    url(r'^(?P<year>d{4})/$','events.views.year'), 
)

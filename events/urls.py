'''
Created on Jun 17, 2013

@author: taylorak
'''

from django.conf.urls import patterns, url
#from django.views.generic import ListView, DetailView
#from events.models import event, announcement 

urlpatterns = patterns('',
    url(r'^$', 'events.views.index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$','events.views.month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$','events.views.day'),
#    url(r'^(?P<year>d{4})/$','events.views.year'), 
)

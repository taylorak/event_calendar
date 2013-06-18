'''
Created on Jun 17, 2013

@author: taylorak
'''

from django.conf.urls import patterns, include, url
#from django.views.generic import ListView, DetailView
#from events.models import event, announcement 

urlpatterns = patterns('',
    url(r'^$', 'events.views.index'),
)


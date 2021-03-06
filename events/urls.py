'''
Created on Jun 17, 2013

@author: taylorak
'''
#from djang.conf.urls.defaults import *
from django.conf.urls import patterns, url
#from django.views.generic import ListView, DetailView
#from events.models import event, announcement 
from events.feeds import LatestAnnouncement

#feeds = {
#         'announcements': LatestAnnouncement(),
#}

urlpatterns = patterns('',
    url(r'^$', 'events.views.event_calendar'),
    url(r'^events/(?P<e_id>\d+)/$','events.views.event_details'),
    url(r'^announcements/(?P<a_id>\d+)/$','events.views.announcement_details'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$','events.views.month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$','events.views.day'),
    url(r'^add_event/$','events.views.add_event'),
    url(r'^add_announcement/$','events.views.add_announcement'),
#    url(r'^feeds/announcements/$',LatestAnnouncement()),
#    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
#    {'feed_dict': feeds}),
#    url(r'^profile/$','events.views.profile'),
#    url(r'^(?P<year>d{4})/$','events.views.year'), 
)


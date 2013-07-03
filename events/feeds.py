'''
Created on Jun 29, 2013

@author: taylorak
'''
from django.contrib.syndication.views import Feed
#from django.utils.feedgenerator import Atom1Feed
from models import announcement

class LatestAnnouncement(Feed):
    title = "New Announcements"
    link = "/calendar/"
    description = "The latest announcements."
#    feed_type = Atom1Feed
    
#    title_template = "feeds/announcements_title"
    description_template = "feeds/announcements_description.html"
    
    def items(self):
 #       import datetime
 #       date = datetime.date.today()
    
        announcement_list = announcement.objects.all()#.filter(expire_date__gt=date).order_by('-entry_date')
        return announcement_list
   
    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.get_absolute_url()

#    def item_description(self, item):
#        return item.description
    

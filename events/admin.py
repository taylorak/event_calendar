'''
Created on Jun 17, 2013

@author: taylorak
'''
from django.contrib import admin
from models import announcement, event

class AdminEvent(admin.ModelAdmin):
    list_display = ['short_title', 'title']  

class AdminAnnouncement(admin.ModelAdmin):
    list_display = ['poster', 'title', 'person_id']
     
admin.site.register(event, AdminEvent)
admin.site.register(announcement, AdminAnnouncement)
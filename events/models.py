from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import datetime
from widgets import SplitSelectDateTimeWidget

# Create your models here.

class announcement(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    description = models.TextField()
    expire_date = models.DateTimeField()
    entry_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return str(self.entry_date)


class announcement_Form(ModelForm):
    #expire_date = forms.DateField(widget = SelectDateWidget, required=True)
    expire_date = forms.DateField(widget=SelectDateWidget, initial=datetime.date.today(), required=True)
    class Meta:
        model = announcement
        exclude = ('author','entry_date')

####

class event(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=64)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    
    def __unicode__(self):
        return str(self.start_date)

class event_Form(ModelForm):
    start_date = forms.DateTimeField(label = "Start Date/Time", widget = SplitSelectDateTimeWidget(twelve_hr=True,hour_step=1,minute_step=5,second_step=10),initial=datetime.datetime.now(),required=True, help_text ="24-hour clock (00:00 - 23:59)")
    end_date = forms.DateTimeField(label = "End Date/Time", widget = SplitSelectDateTimeWidget(twelve_hr=True,hour_step=1,minute_step=5,second_step=10),initial=datetime.datetime.now(),required=True, help_text ="24-hour clock (00:00 - 23:59)")

    class Meta:
        model = event
        exclude = ('author')

####

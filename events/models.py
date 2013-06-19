from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from widgets import SelectDateWidget,SplitSelDateTimeWidget

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
    expire_date = forms.DateField(widget = SelectDateWidget, required=True)

    class Meta:
        model = announcement
        exclude = ('poster','entry_date', 'person_id')


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
    start_date = forms.DateTimeField(label = "Start Date/Time", widget = SplitSelDateTimeWidget, required=True, help_text ="24-hour clock (00:00 - 23:59)")
    end_date = forms.DateTimeField(label = "End Date/Time", widget = SplitSelDateTimeWidget, required=True, help_text ="24-hour clock (00:00 - 23:59)")

    class Meta:
        model = event
        exclude = ('person_id')

####

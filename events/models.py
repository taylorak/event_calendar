from django import forms
from django.db import models
from django.forms import ModelForm
from widgets import SelectDateWidget,SplitSelDateTimeWidget

# Create your models here.
class people(models.Model):
    pass

class department(models.Model):
    pass

class announcement(models.Model):
    id = models.AutoField('annoucement_id', primary_key=True)
    person_id = models.ForeignKey(people,verbose_name="Contact", related_name = "contact")
    title = models.CharField(max_length=300)
    description = models.TextField()
    expire_date = models.DateTimeField()
    entry_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)
    poster = models.ForeignKey(people)    


class announcement_Form(ModelForm):
    expire_date = forms.DateField(widget = SelectDateWidget, required=True)

    class Meta:
        model = announcement
        exclude = ('poster','entry_date', 'person_id')


####

class event(models.Model):
    id = models.AutoField('event_id', primary_key=True)
    person_id = models.ForeignKey(people)
    dept_id = models.ForeignKey(department)
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=64)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=64)
    description = models.TextField()
    presenter = models.CharField(max_length=64, blank = True, null = True)
    url =  models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return str(self.start_date)

class event_Form(ModelForm):
    start_date = forms.DateTimeField(label = "Start Date/Time", widget = SplitSelDateTimeWidget, required=True, help_text ="24-hour clock (00:00 - 23:59)")
    end_date = forms.DateTimeField(label = "End Date/Time", widget = SplitSelDateTimeWidget, required=True, help_text ="24-hour clock (00:00 - 23:59)")

    class Meta:
        model = event
        exclude = ('person_id')

####

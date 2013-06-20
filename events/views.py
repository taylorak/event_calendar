# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import event, announcement

def index(request):
    # Test, change later
    import datetime
    date = datetime.date.today()
    event_list = event.objects.all().order_by('-start_date')[:5]
    announcement_list = announcement.objects.all().order_by('-entry_date')[:5]
    return render_to_response('events/index.html',{'event_list':event_list,'announcement_list':announcement_list,'year':date.year,'month':date.month})

def month(request,year,month):
    year,month = int(year),int(month)
    event_list = event.objects.filter(start_date__year=year,start_date__month=month).order_by('-start_date')
    announcement_list = announcement.objects.filter(entry_date__year=year,entry_date__month=month).order_by('-entry_date')
    return render_to_response('events/index.html',{'event_list':event_list,'announcement_list':announcement_list,'year':year,'month':month})

def day(request,year,month,day):
    year,month,day = int(year),int(month),int(day)
    event_list = event.objects.filter(start_date__year=year,start_date__month=month,start_date__day=day).order_by('-start_date')
    announcement_list = announcement.objects.filter(entry_date__year=year,entry_date__month=month,entry_date__day=day).order_by('-entry_date')
    return render_to_response('events/index.html',{'event_list':event_list,'announcement_list':announcement_list,'year':year,'month':month})

# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from models import event, announcement

def index(request):
    # Test, change later
    import datetime
    date = datetime.date.today()
    event_list = event.objects.all().order_by('-start_date')[:5]
    announcement_list = announcement.objects.all().order_by('-entry_date')[:5]
    return render_to_response('events/index.html',{'event_list':event_list,'announcement_list':announcement_list,'year':date.year,'month':date.month})

def event_details(request,e_id):
    event_details = get_object_or_404(event,id=e_id)
    return render_to_response('events/event_details.html',{'event': event_details,'year':event_details.start_date.year,'month':event_details.start_date.month})

def announcement_details(request,a_id):
    announcement_details = get_object_or_404(announcement,id=a_id)
    return render_to_response('events/announcement_details.html',{'announcement': announcement_details,'year':announcement_details.entry_date.year,'month':announcement_details.entry_date.month})
    
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

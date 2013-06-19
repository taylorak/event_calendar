# Create your views here.

#from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import event, announcement

def index(request):
    # Test, change later
    event_list = event.objects.all().order_by('-start_date')[:5]
    announcement_list = announcement.objects.all().order_by('-entry_date')[:5]
    return render_to_response('events/index.html',{'event_list':event_list,'announcement_list':announcement_list})

def day(request,day):
    pass
def month(request,month,day):
    pass
def year(request,year,month,day):
    pass
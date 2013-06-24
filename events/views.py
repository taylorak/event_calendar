# Create your views here.

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,get_object_or_404
from models import event, announcement, event_Form, announcement_Form
from django.template import RequestContext

def index(request):
    import datetime
    date = datetime.date.today()
    event_list = event.objects.all().filter(start_date__gt=date).order_by('-start_date')[:5]
    announcement_list = announcement.objects.all().filter(expire_date__gt=date).order_by('-entry_date')
    c = {'event_list':event_list,'announcement_list':announcement_list,'year':date.year,'month':date.month,'day':date.day}
    return render_to_response('index.html', RequestContext(request, c))

def event_details(request,e_id):
    event_details = get_object_or_404(event,id=e_id)
    c = {'event': event_details,'year':event_details.start_date.year,'month':event_details.start_date.month}
    return render_to_response('events/event_details.html',RequestContext(request, c))

def announcement_details(request,a_id):
    announcement_details = get_object_or_404(announcement,id=a_id)
    c = {'announcement': announcement_details,'year':announcement_details.entry_date.year,'month':announcement_details.entry_date.month}
    return render_to_response('events/announcement_details.html',RequestContext(request, c))
    
def month(request,year,month):
    year,month = int(year),int(month)
    event_list = event.objects.filter(start_date__year=year,start_date__month=month).order_by('-start_date')
    c = {'event_list':event_list,'year':year,'month':month}
    return render_to_response('events/event_calendar.html',RequestContext(request, c))

def day(request,year,month,day):
    year,month,day = int(year),int(month),int(day)
    event_list = event.objects.filter(start_date__year=year,start_date__month=month,start_date__day=day).order_by('-start_date')
    c = {'event_list':event_list,'year':year,'month':month}
    return render_to_response('events/event_calendar.html',RequestContext(request, c))

@login_required
def add_event(request):
    if request.method == 'POST':
        form = event_Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/calendar/profile')
    else:
        form = event_Form()
    c = {'message': 'Add Event','form': form}
    return render_to_response('forms/add.html',RequestContext(request, c))

@login_required
def add_announcement(request):
    if request.method == 'POST':
        form = announcement_Form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/calendar/profile')
    else:   
        form = announcement_Form()
    c = {'message': 'Add Announcement', 'form': form}
    return render_to_response('forms/add.html',RequestContext(request, c))
    
@login_required
def profile(request):
    event_list = event.objects.filter(author=request.user).order_by('-start_date')
    announcement_list = announcement.objects.all().filter(author=request.user).order_by('-entry_date')
    c = {'event_list':event_list,'announcement_list':announcement_list}
    return render_to_response('profile.html',RequestContext(request, c))

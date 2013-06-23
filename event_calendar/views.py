'''
Created on Jun 22, 2013

@author: taylorak
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from events.models import event,announcement
from django.template import RequestContext

@login_required
def profile(request):
    event_list = event.objects.filter(author=request.user).order_by('-start_date')
    announcement_list = announcement.objects.all().filter(author=request.user).order_by('entry_date')
    c = {'event_list':event_list,'announcement_list':announcement_list}
    return render_to_response('profile.html',RequestContext(request, c))
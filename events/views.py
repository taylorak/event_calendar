# Create your views here.

from django.http import HttpResponse

def index(request):
    # Test, change later
    html = "<h1>Hello World</h1>"
    return HttpResponse(html)
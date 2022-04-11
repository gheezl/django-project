from django.http import HttpResponse

# Create your views here.

def console_log():
    return HttpResponse("Hello World")
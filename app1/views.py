from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return render(request,'first.html')

def string_response(request):
    return HttpResponse('<marquee><h1>string response of app1</marquee></h1>')

def second(request):
    return render(request,'second.html')
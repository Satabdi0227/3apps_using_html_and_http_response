from django.shortcuts import render
from django.http import HttpResponse


def app3_F(request):
    return render(request,'app3_F.html')

def str_res(request):
    return HttpResponse('<marquee><h1>string response of app3</marquee></h1>')

def app3_S(request):
    return render(request,'app3_S.html')

# Create your views here.

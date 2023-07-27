from django.shortcuts import render
from django.http import HttpResponse

def app2_F(request):
    return render(request,'app2_F.html')

def str_res(request):
    return HttpResponse('<marquee><h1>string response of app2</marquee></h1>')

def app2_S(request):
    return render(request,'app2_S.html')

# Create your views here.

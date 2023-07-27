from django.urls import path
from app3.views import *
app_name = 'three'

urlpatterns = [
    path('app3_F/',app3_F,name='app3_F'),
    path('str_res/',str_res,name='str_res'),
    path('app3_S/',app3_S,name='app3_S'),
]
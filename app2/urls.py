from django.urls import path
from app2.views import *

urlpatterns = [
    path('app2_F/',app2_F,name='app2_F'),
    path('str_res/',str_res,name='str_res'),
    path('app2_S/',app2_S,name='app2_S'),
]
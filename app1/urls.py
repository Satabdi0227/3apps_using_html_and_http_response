from django.urls import path
from app1.views import *

app_name='anything'

urlpatterns = [
    path('first/',first,name='first'),
    path('string_response/',string_response,name='string_response'),
    path('second/',second,name = 'second'),
]
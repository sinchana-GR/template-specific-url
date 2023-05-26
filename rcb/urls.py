from django.urls import path
from rcb.views import *
app_name='someting'
urlpatterns=[
    path('virat/',virat,name='virat'),
]
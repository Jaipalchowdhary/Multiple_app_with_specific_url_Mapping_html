app_name='something'
from django.urls import path
from rcb.views import *

urlpatterns=[

    path('virat/',virat,name='virat'),
]
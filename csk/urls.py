app_name='anything'
from django.urls import path
from csk.views import *

urlpatterns=[

    path('msd/',msd,name='msd'),
]
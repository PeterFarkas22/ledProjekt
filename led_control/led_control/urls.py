from django.contrib import admin
from django.urls import path
from control.views import index, turn_on, turn_off, motor

urlpatterns = [
    path('', index, name='index'),
    path('turn-on/', turn_on, name='turn_on'),
    path('turn-off/', turn_off, name='turn_off'),
    path('motor/', motor, name='motor'),
]
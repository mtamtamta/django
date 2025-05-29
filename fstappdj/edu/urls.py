from django.urls import path
from . import views

app_name = 'edu'

urlpatterns = [
    path('',      views.entry_list,   name='entry_list'),
    path('add/',  views.entry_create, name='entry_create'),
]

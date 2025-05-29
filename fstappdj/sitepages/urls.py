from django.urls import path
from . import views

app_name = 'sitepages'

urlpatterns = [
    # «Я»
    path('me/',       views.me_list,     name='me_list'),
    path('me/add/',   views.me_create,   name='me_create'),

    # «ОП»
    path('program/',      views.program_list,   name='program_list'),
    path('program/add/',  views.program_create, name='program_create'),

    # «Менеджмент»
    path('management/',            views.management_list,       name='management_list'),
    path('management/sup/add/',    views.supervisor_create,     name='supervisor_create'),
    path('management/mgr/add/',    views.manager_create,        name='manager_create'),

    # «Сокурсники»
    path('classmates/',        views.classmates_list,    name='classmates_list'),
    path('classmates/add/',    views.classmate_create,   name='classmate_create'),
]

from django.contrib import admin
from .models import Me, Program, Supervisor, Manager, Classmate

@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display   = ('full_name', 'email', 'phone')
    search_fields  = ('full_name', 'email')
    list_filter    = ('email',)  # при желании можно убрать

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display   = ('name',)
    search_fields  = ('name',)

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display   = ('full_name', 'email', 'phone')
    search_fields  = ('full_name', 'email')
    list_filter    = ('full_name',)

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display   = ('full_name', 'email')
    search_fields  = ('full_name', 'email')

@admin.register(Classmate)
class ClassmateAdmin(admin.ModelAdmin):
    list_display   = ('full_name', 'email', 'phone')
    search_fields  = ('full_name', 'email')

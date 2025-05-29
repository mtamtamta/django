from django.contrib import admin
from .models import (
    ProgramEntry,
)

@admin.register(ProgramEntry)
class ProgramEntryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'program_name', 'year_of_admission', 'gpa')
    list_filter = ('program_name', 'year_of_admission')
    search_fields = ('full_name', 'program_name')
    ordering = ('-year_of_admission',)
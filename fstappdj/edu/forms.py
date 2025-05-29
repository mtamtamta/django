from django import forms
from .models import ProgramEntry

class ProgramEntryForm(forms.ModelForm):
    class Meta:
        model = ProgramEntry
        fields = ['full_name', 'program_name', 'year_of_admission', 'gpa']

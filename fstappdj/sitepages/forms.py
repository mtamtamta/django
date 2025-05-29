from django import forms
from .models import Me, Program, Supervisor, Manager, Classmate

class MeForm(forms.ModelForm):
    class Meta:
        model = Me
        fields = ['full_name', 'photo', 'email', 'phone', 'resume']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'study_content', 'learning_outcomes', 'advantages', 'prospects']

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = ['full_name', 'photo', 'email', 'phone']

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['full_name', 'photo', 'email']

class ClassmateForm(forms.ModelForm):
    class Meta:
        model = Classmate
        fields = ['full_name', 'photo', 'email', 'phone']

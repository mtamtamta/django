from django.db import models
from django.urls import reverse

class ProgramEntry(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    program_name = models.CharField("Программа обучения", max_length=100)
    year_of_admission = models.IntegerField("Год поступления")
    gpa = models.DecimalField("Средний балл (GPA)", max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.full_name} — {self.program_name}"
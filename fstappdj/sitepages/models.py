from django.db import models

class Me(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    photo     = models.ImageField("Фото", upload_to="sitepages/me/")
    email     = models.EmailField("Email")
    phone     = models.CharField("Телефон", max_length=20)
    resume    = models.TextField("Резюме")

    def __str__(self):
        return self.full_name


class Program(models.Model):
    name              = models.CharField("Название ОП", max_length=200)
    study_content     = models.TextField("Что буду изучать")
    learning_outcomes = models.TextField("Чему научусь")
    advantages        = models.TextField("Преимущества")
    prospects         = models.TextField("Перспективы")

    def __str__(self):
        return self.name


class Supervisor(models.Model):
    full_name = models.CharField("Академический руководитель", max_length=100)
    photo     = models.ImageField("Фото", upload_to="sitepages/supervisors/")
    email     = models.EmailField("Email")
    phone     = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.full_name


class Manager(models.Model):
    full_name = models.CharField("Менеджер ОП", max_length=100)
    photo     = models.ImageField("Фото", upload_to="sitepages/managers/")
    email     = models.EmailField("Email")

    def __str__(self):
        return self.full_name


class Classmate(models.Model):
    full_name = models.CharField("Сокурсник", max_length=100)
    photo     = models.ImageField("Фото", upload_to="sitepages/classmates/")
    email     = models.EmailField("Email")
    phone     = models.CharField("Телефон", max_length=20)

    def __str__(self):
        return self.full_name
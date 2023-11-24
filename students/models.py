from django.db import models

from educational_modules.models import Modules
from users.models import NULLABLE


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='educational-modules/students/photo', verbose_name='фото студента', **NULLABLE)
    email = models.EmailField(max_length=150, unique=True, verbose_name='почта', **NULLABLE)
    phone = models.CharField(max_length=20, unique=True, verbose_name='номер телефона', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')
    modul = models.ForeignKey(Modules, verbose_name="образовательный модуль", on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['first_name', "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
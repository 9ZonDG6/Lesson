from django.db import models
from django.db.models import CharField


class Car(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self) -> CharField:
        return self.name


class Plane(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'

    def __str__(self) -> CharField:
        return self.name

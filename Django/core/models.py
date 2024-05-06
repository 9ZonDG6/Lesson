from django.db import models
from django.db.models import CharField


class Car(models.Model):

    TYPE_CHOICES = (
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electricity', 'Электричество'),
        ('hybrid', 'Гибрид'),
    )

    brand = models.CharField('Марка', max_length=40)
    model = models.CharField('Модель', max_length=40)
    fuel = models.CharField('Топливо', max_length=15, choices=TYPE_CHOICES, default='patrol')
    information = models.TextField('Информация', blank=True)
    horsepower = models.PositiveSmallIntegerField('Лошадиная сила', default=0)
    released = models.BooleanField('Выпускается', default=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self) -> str:
        return f'{self.brand} {self.model}'


class Plane(models.Model):

    name = models.CharField('Название', max_length=100)
    capacity = models.PositiveSmallIntegerField('Вместимость', default=0)
    passenger = models.BooleanField('Пассажирский', default=True)

    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'

    def __str__(self) -> CharField:
        return self.name

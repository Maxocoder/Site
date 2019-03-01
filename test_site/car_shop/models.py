from django.db import models


class BaseRegister(models.Model):
    firstname = models.CharField(verbose_name='Имя', max_length=200, db_index=True, default="")
    lastname = models.CharField(verbose_name='Фамилия', max_length=200,  default="")
    reporting = models.CharField(verbose_name='Отчество', max_length=200, default="")
    email = models.EmailField(verbose_name='E-Mail', max_length=200, default="")
    auto = models.CharField(verbose_name='Автомобиль', max_length=200,  default="")
    profi = models.CharField(verbose_name='Специалист, выполняющий заказ', max_length=200, default="")
    date = models.DateTimeField(verbose_name='Время записи', default="")


    class Meta:
        verbose_name = 'Зарегестрированные на диагностику'
        verbose_name_plural = 'Зарегестрированные на диагностику'

    def __str__(self):
        return self.lastname


from django.db import models


# Create your models here.
class FirstTable(models.Model):
    name = models.CharField('Название', max_length=40)
    main_text = models.TextField('Содержание', max_length=10000)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Причину'
        verbose_name_plural = 'Причины'


class Commentaries(models.Model):
    author = models.CharField('Автор', max_length=20)
    commentary = models.TextField('Содержание', max_length=500)
    date = models.DateTimeField('Дата')
    nameb = models.CharField('Привязка', max_length=40)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

from django.db import models


# Create your models here.
class FirstTable(models.Model):
    name = models.CharField('Fish name', max_length=40)
    main_text = models.TextField('Main text', max_length=10000)
    date = models.DateField('Date')
    img = models.FileField('Image', upload_to='img/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'fish'
        verbose_name_plural = 'fishes'

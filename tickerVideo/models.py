from django.db import models


# Create your models here.
class Ticker(models.Model):
    text_ticker = models.CharField(max_length=500, verbose_name="Текст бегущей строки")
    link_to_video = models.CharField(max_length=500, verbose_name="Ссылка на видео")

    def __str__(self):
        return self.text_ticker

    class Meta:
        verbose_name = 'Бегущая строка'
        verbose_name_plural = "Бегущие строки"

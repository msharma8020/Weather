from django.db import models

# Create your models here.

class Weather(models.Model):
    city_name = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = "cities"
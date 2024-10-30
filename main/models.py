from django.db import models

# Create your models here.
class Main(models.Model):
    title=models.CharField(
        verbose_name="имя",
        max_length=255
    )
    description=models.CharField(
        verbose_name="описание",
        max_length=255

    )
    photo=models.ImageField(
        verbose_name="фото"
    )
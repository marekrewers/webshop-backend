from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nazwa kategorii')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategorie"

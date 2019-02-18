from django.db import models
from categories.models import Category


class Card(models.Model):
    categories = models.ManyToManyField(Category)
    isFeatured = models.BooleanField(default=False, verbose_name='Promowany')
    name = models.CharField(max_length=150, verbose_name='Tytuł')
    description = models.TextField(verbose_name='Opis')
    photoUrl = models.ImageField(upload_to='images/cards/', default='/images/cards/default.jpg', verbose_name='Zdjęcie')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kartki"

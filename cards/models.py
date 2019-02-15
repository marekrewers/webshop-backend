from django.db import models

# Create your models here.


class Card(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/cards/', default='/static/images/cards/default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Cards"

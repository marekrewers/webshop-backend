from django.contrib import admin

# Register your models here.
from .models import Card

admin.site.register(Card)

admin.site.site_header = "CARDART"

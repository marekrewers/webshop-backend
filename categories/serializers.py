from rest_framework import serializers
from .models import Category


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        class Meta:
            model = Category

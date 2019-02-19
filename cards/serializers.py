from rest_framework import serializers
from .models import Card
from categories.serializers import CategoriesSerializer


class CardSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)

    class Meta:
        model = Card
        fields = "__all__"

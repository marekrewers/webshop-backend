from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    category_name = serializers.RelatedField(source='category.name', read_only='True')

    class Meta:
        model = Card
        fields = "__all__"
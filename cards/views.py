from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer


class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class FeaturedCardView(viewsets.ModelViewSet):
    queryset = Card.objects.filter(isFeatured=True)
    serializer_class = CardSerializer

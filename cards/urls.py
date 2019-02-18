from rest_framework import routers
from django.urls import path, include
from .views import CardView
from .views import FeaturedCardView


router = routers.DefaultRouter()
router.register('all', CardView)
router.register('featured', FeaturedCardView)

urlpatterns = [
    path('', include(router.urls)),
]

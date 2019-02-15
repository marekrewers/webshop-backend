from rest_framework import routers
from django.urls import path, include
from .views import CardView


router = routers.DefaultRouter()
router.register(r'', CardView)
router.register(r'', CardView)

urlpatterns = [
    path('', include(router.urls))
]

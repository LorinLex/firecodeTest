from rest_framework import routers
from .views import CityViewSet, ShopViewSet
from django.urls import include, path

router = routers.SimpleRouter()
router.register(r'city', CityViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from .filters import ShopFilter


class CityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(methods=['GET'], detail=True)
    def street(self, request, pk):
        queryset = Street.objects.filter(city_id=pk)
        serializer = StreetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShopViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    queryset = Shop.objects.select_related('city_id', 'street_id').all()
    serializer_class = ShopSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

from django.utils.decorators import method_decorator
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, \
    ShopListSerializer, ShopCreateSerializer
from .filters import ShopFilter
from drf_yasg.utils import swagger_auto_schema


class CityViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(methods=['GET'], detail=True)
    @swagger_auto_schema(
        responses={
            200: StreetSerializer(many=True),
            400: "{\"detail\": \<error\>}",
        }
    )
    def street(self, request, pk):
        try:
            queryset = Street.objects.select_related('city').filter(city_id=pk)
            serializer = StreetSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'detail': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


@method_decorator(name='create', decorator=swagger_auto_schema(
    responses={
        200: "{\"id\": \<new shop id\>}",
        400: "{\<field\>: \<error\>}",
    }
))
class ShopViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):
    queryset = Shop.objects.select_related('city', 'street').all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopListSerializer
        return ShopCreateSerializer

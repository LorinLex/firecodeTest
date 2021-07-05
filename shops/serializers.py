from rest_framework.serializers import ModelSerializer, CharField, \
    SerializerMethodField
from . import models


class CitySerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class StreetSerializer(ModelSerializer):
    class Meta:
        model = models.Street
        # fields = '__all__'
        exclude = ['city_id']


class ShopSerializer(ModelSerializer):
    city = CharField(read_only=True, source='city_id.name')
    street = CharField(read_only=True, source='street_id.name')

    class Meta:
        model = models.Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'open']

from rest_framework.serializers import ModelSerializer, CharField, ReadOnlyField
from . import models


class CitySerializer(ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class StreetSerializer(ModelSerializer):
    city = CharField(read_only=True, source='city.name')

    class Meta:
        model = models.Street
        fields = ['id', 'name', 'city']


class ShopListSerializer(ModelSerializer):
    city = CharField(read_only=True, source='city.name')
    street = CharField(read_only=True, source='street.name')
    open = ReadOnlyField()

    class Meta:
        model = models.Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'open']


class ShopCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Shop
        fields = [
            'id',
            'name',
            'city',
            'street',
            'house',
            'opening_time',
            'closing_time'
        ]
        extra_kwargs = {
            'name': {
                'write_only': True
            },
            'city': {
                'write_only': True
            },
            'street': {
                'write_only': True
            },
            'house': {
                'write_only': True
            },
            'opening_time': {
                'write_only': True
            },
            'closing_time': {
                'write_only': True
            },
        }

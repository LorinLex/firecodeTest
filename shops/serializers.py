from rest_framework.serializers import ModelSerializer, CharField, \
    SerializerMethodField
from . import models
from datetime import datetime


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
    open = SerializerMethodField(read_only=True, method_name='is_open')

    class Meta:
        model = models.Shop
        fields = ['id', 'name', 'city', 'street', 'house', 'open']

    @staticmethod
    def is_open(instance):
        if instance.opening_time < datetime.now().time()\
                < instance.closing_time:
            return True
        return False

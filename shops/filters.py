import django_filters
from .models import Shop
from datetime import datetime
from django.db.models import Q


class ShopFilter(django_filters.FilterSet):
    open = django_filters.NumberFilter(
        field_name='opening_time', method='is_open', label="open")
    street = django_filters.CharFilter(
        field_name='street_id__name', label="street")
    city = django_filters.CharFilter(
        field_name='city_id__name', label="city")

    class Meta:
        model = Shop
        fields = ('open', 'street', 'city')

    def is_open(self, queryset, name, value):
        if value == 1:
            return queryset.filter(closing_time__gte=datetime.now().time(),
                                   opening_time__lte=datetime.now().time())
        return queryset.filter(Q(closing_time__lte=datetime.now().time()) |
                               Q(opening_time__gte=datetime.now().time()))

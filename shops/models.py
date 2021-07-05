from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)


class Street(models.Model):
    name = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

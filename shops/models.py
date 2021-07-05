from django.db import models
from datetime import datetime


class City(models.Model):
    name = models.CharField(max_length=50)


class Street(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house = models.CharField(max_length=10)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    @property
    def open(self):
        if self.opening_time < datetime.now().time() < self.closing_time:
            return True
        return False

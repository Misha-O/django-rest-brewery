from django.db import models
from datetime import datetime


class Beer(models.Model):

    name = models.CharField(max_length=60)
    brewery_name = models.CharField(max_length=60)
    alcohol_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(
        'created_at', default=datetime.now, blank=True, editable=False)

    def __str__(self):
        return self.name


class Water(models.Model):
    beer_id = models.ForeignKey(
        Beer, on_delete=models.CASCADE, related_name='water')
    name = models.CharField(max_length=60, default='spring water')
    created_at = models.DateTimeField(
        'created_at', default=datetime.now, blank=True, editable=False)

    def __str__(self):
        return self.name


class Hop(models.Model):
    beer_id = models.ForeignKey(
        Beer, on_delete=models.CASCADE, related_name='hop')
    name = models.CharField(max_length=60, default=None)
    created_at = models.DateTimeField(
        'created_at', default=datetime.now, blank=True, editable=False)

    def __str__(self):
        return self.name


class Malt(models.Model):
    beer_id = models.ForeignKey(
        Beer, on_delete=models.CASCADE, related_name='malt')
    name = models.CharField(max_length=60, default=None)
    created_at = models.DateTimeField(
        'created_at', default=datetime.now, blank=True, editable=False)

    def __str__(self):
        return self.name

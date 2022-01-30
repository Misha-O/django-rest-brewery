from .models import Beer, Water, Hop, Malt
from rest_framework import serializers

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ['name']

class HopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hop
        fields = ['name']

class MaltSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malt
        fields = ['name']

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    water = WaterSerializer(many=False)
    hop = HopSerializer(many=True)
    malt = MaltSerializer(many=True)
    class Meta:
        model = Beer
        fields = ('id', 'name', 'brewery_name', 'alcohol_percentage', 'price', 'water', 'hop', 'malt', 'created_at')
from django.db.models.base import Model
from rest_framework import serializers

from .models import Pokemon, Stat, Multiplier


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)



class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'


class MultiplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multiplier
        fields = '__all__'

from django.db.models.base import Model
from rest_framework import serializers

from .models import Pokemon, Stats, Multipliers


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


# class PokemonCSVSerializer(serializers.Serializer):

#     pokedex_id = serializers.IntegerField()
#     name = serializers.CharField()
#     japanese_name = serializers.CharField()
#     generation = serializers.IntegerField()
#     classification = serializers.CharField()
#     is_legendary = serializers.BooleanField()
#     abilities = serializers.ListField(child=serializers.CharField())
#     type_1 = serializers.CharField()
#     type_2 = serializers.CharField()

#     attack = serializers.IntegerField()
#     special_atk = serializers.IntegerField()
#     defense = serializers.IntegerField()
#     special_def = serializers.IntegerField()
#     hit_points = serializers.IntegerField()
#     weight = serializers.FloatField()
#     height = serializers.FloatField()
#     speed = serializers.IntegerField()
#     capture_rate = serializers.FloatField()

#     against_bug = serializers.FloatField()
#     against_dark = serializers.FloatField()
#     against_dragon = serializers.FloatField()
#     against_electric = serializers.FloatField()
#     against_fairy = serializers.FloatField()
#     against_fight = serializers.FloatField()
#     against_fire = serializers.FloatField()
#     against_flying = serializers.FloatField()
#     against_ghost = serializers.FloatField()
#     against_grass = serializers.FloatField()
#     against_ground = serializers.FloatField()
#     against_ice = serializers.FloatField()
#     against_normal = serializers.FloatField()
#     against_poison = serializers.FloatField()
#     against_psychic = serializers.FloatField()
#     against_rock = serializers.FloatField()
#     against_steel = serializers.FloatField()
#     against_water = serializers.FloatField()

#     def create(self, validated_data):
#         return Pokemon.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.body = validated_data.get('body', instance.body)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)

#         instance.save()
#         return instance


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'


class MultiplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multipliers
        fields = '__all__'

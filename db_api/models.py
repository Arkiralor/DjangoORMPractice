from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.


class Pokemon(models.Model):
    '''
    Model/Table to contain basic information for each pokemon:
    '''

    pokedex_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    japanese_name = models.CharField(max_length=32)
    generation = models.IntegerField(null=True)
    classification = models.CharField(max_length=64)
    is_legendary = models.BooleanField(default=False)
    abilities = ArrayField(models.CharField(max_length=32))
    type_1 = models.CharField(max_length=16)
    type_2 = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.pokedex_id}. {self.name}"

    class Meta:
        verbose_name_plural = 'pokemon'
        unique_together = ['pokedex_id', 'name', 'japanese_name']


class Stat(models.Model):
    '''
    Model/Table to contain basic stats for each pokemon:
    '''
    pokedex_id = models.ForeignKey(Pokemon, on_delete=CASCADE)
    attack = models.IntegerField(default=1)
    special_atk = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    special_def = models.IntegerField(default=1)
    hit_points = models.IntegerField(default=1)
    weight = models.FloatField(default=-1.5)
    height = models.FloatField(default=-1.5)
    speed = models.IntegerField(default=0)
    capture_rate = models.FloatField(default=-1.5)

    def __str__(self):
        return str(self.pokedex_id.pokedex_id)

    class Meta:
        verbose_name_plural = 'stats'
        unique_together = ['pokedex_id']


class Multiplier(models.Model):
    '''
    Model/Table to contain the multipliers against various types for each pokemon:
    '''
    pokedex_id = models.ForeignKey(Pokemon, on_delete=CASCADE)
    against_bug = models.FloatField(default=-1.5)
    against_dark = models.FloatField(default=-1.5)
    against_dragon = models.FloatField(default=-1.5)
    against_electric = models.FloatField(default=-1.5)
    against_fairy = models.FloatField(default=-1.5)
    against_fight = models.FloatField(default=-1.5)
    against_fire = models.FloatField(default=-1.5)
    against_flying = models.FloatField(default=-1.5)
    against_ghost = models.FloatField(default=-1.5)
    against_grass = models.FloatField(default=-1.5)
    against_ground = models.FloatField(default=-1.5)
    against_ice = models.FloatField(default=-1.5)
    against_normal = models.FloatField(default=-1.5)
    against_poison = models.FloatField(default=-1.5)
    against_psychic = models.FloatField(default=-1.5)
    against_rock = models.FloatField(default=-1.5)
    against_steel = models.FloatField(default=-1.5)
    against_water = models.FloatField(default=-1.5)

    def __str__(self):
        return str(self.pokedex_id.pokedex_id)

    class Meta:
        verbose_name_plural = 'multipliers'
        unique_together = ['pokedex_id']

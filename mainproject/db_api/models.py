from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE

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
    is_legendary = models.BooleanField()
    abilities = ArrayField(models.CharField(max_length=32))
    type_1 = models.CharField(max_length=16)
    type_2 = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.pokedex_id}. {self.name}"

    class Meta:
        verbose_name_plural = 'pokemon'


class Stats(models.Model):
    '''
    Model/Table to contain basic stats for each pokemon:
    '''

    pokedex_id = models.ForeignKey(Pokemon, on_delete=CASCADE)
    attack = models.IntegerField()
    special_atk = models.IntegerField()
    defense = models.IntegerField()
    special_def = models.IntegerField()
    hit_points = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.IntegerField()
    capture_rate = models.FloatField()

    def __str__(self):
        return self.stat_id

    class Meta:
        verbose_name_plural = 'stats'


class Multipliers(models.Model):
    '''
    Model/Table to contain the multipliers against various types for each pokemon:
    '''

    pokedex_id = models.ForeignKey(Pokemon, on_delete=CASCADE)
    against_bug = models.FloatField()
    against_dark = models.FloatField()
    against_dragon = models.FloatField()
    against_electric = models.FloatField()
    against_fairy = models.FloatField()
    against_fight = models.FloatField()
    against_fire = models.FloatField()
    against_flying = models.FloatField()
    against_ghost = models.FloatField()
    against_grass = models.FloatField()
    against_ground = models.FloatField()
    against_ice = models.FloatField()
    against_normal = models.FloatField()
    against_poison = models.FloatField()
    against_psychic = models.FloatField()
    against_rock = models.FloatField()
    against_steel = models.FloatField()
    against_water = models.FloatField()

    def __str__(self):
        return self.mult_id

    class Meta:
        verbose_name_plural = 'multipliers'

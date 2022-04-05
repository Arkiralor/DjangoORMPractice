from django.contrib import admin
from .models import Pokemon, Stat, Multiplier

# Register your models here.

# admin.site.register(Pokemon)
# admin.site.register(Stat)
# admin.site.register(Multiplier)

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        'pokedex_id', 'name', 'japanese_name', 
        'generation', 'classification', 'is_legendary', 
        'abilities', 'type_1', 'type_2'
        )
    list_filter = ( 
        'generation', 'is_legendary', 'type_1', 'type_2'
        )
    search_fields = (
        'pokedex_id', 'name', 'japanese_name', 
        'generation', 'classification', 'is_legendary', 
        'abilities', 'type_1', 'type_2'
        )


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = (
        'pokedex_id', 'attack', 'special_atk', 
        'defense', 'special_def', 'hit_points', 
        'weight', 'height', 'speed', 'capture_rate'
        )
    raw_id_fields = ('pokedex_id',)
    
    search_fields = (
        'pokedex_id', 'attack', 'special_atk', 
        'defense', 'special_def', 'hit_points', 
        'weight', 'height', 'speed', 'capture_rate'
        )


@admin.register(Multiplier)
class MultiplierAdmin(admin.ModelAdmin):
    list_display = (
        'pokedex_id', 
        'against_bug', 'against_dark', 'against_dragon', 
        'against_electric', 'against_fairy', 'against_fight', 
        'against_fire', 'against_flying', 'against_ghost', 
        'against_grass', 'against_ground', 'against_ice', 
        'against_normal', 'against_poison', 'against_psychic', 
        'against_rock', 'against_steel', 'against_water'
        )
    raw_id_fields = ('pokedex_id',)

    search_fields = (
        'pokedex_id', 
        'against_bug', 'against_dark', 'against_dragon', 
        'against_electric', 'against_fairy', 'against_fight', 
        'against_fire', 'against_flying', 'against_ghost', 
        'against_grass', 'against_ground', 'against_ice', 
        'against_normal', 'against_poison', 'against_psychic', 
        'against_rock', 'against_steel', 'against_water'
        )

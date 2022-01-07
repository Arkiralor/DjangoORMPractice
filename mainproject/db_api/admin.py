from django.contrib import admin
from .models import Pokemon, Stats, Multipliers

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Stats)
admin.site.register(Multipliers)

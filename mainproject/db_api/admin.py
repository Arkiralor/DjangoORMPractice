from django.contrib import admin
from .models import Pokemon, Stat, Multiplier

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Stat)
admin.site.register(Multiplier)

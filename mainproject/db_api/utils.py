from .models import *
from .serializers import *

def get_additional(id:int):
    # stat_query = Stat.objects.get(pokedex_id=id)
    # mult_query = Multiplier.objects.get(pokedex_id=id)

    # stat_serialized = StatSerializer(data=stat_query)
    # mult_serialized = MultiplierSerializer(data=mult_query)
    
    # if stat_serialized.is_valid() and mult_serialized.is_valid():
    #     return {**stat_serialized.data, **mult_serialized.data}
    # else:
    #     return {'error': 'Something broke while retrieving additional details.'}
    stat_query = Stat.objects.get(pokedex_id=id)
    mult_query = Multiplier.objects.get(pokedex_id=id)

    stat_serialized = StatSerializer(stat_query)
    mult_serialized = MultiplierSerializer(mult_query)
    
    return {**stat_serialized.data, **mult_serialized.data}

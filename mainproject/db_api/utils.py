from .models import *
from .serializers import *
import pandas as pd

def get_additional(id:int):
    stat_query = Stat.objects.get(pokedex_id=id)
    mult_query = Multiplier.objects.get(pokedex_id=id)

    stat_serialized = StatSerializer(stat_query)
    mult_serialized = MultiplierSerializer(mult_query)
    
    return {**stat_serialized.data, **mult_serialized.data}

def clean_df(data: pd.DataFrame) -> pd.DataFrame:
    cols = list(data.columns)
    for col in cols:
        data[f"{col}"].fillna(0, inplace = True)
    
    return data

if __name__ == "__main__":
    df = pd.read_csv("D:\Libraries\Arkiralor's Documents\Programs\gits\DjangoORMPractice\datasets\pokemon.csv")
    df_c = clean_df(df)
    df_c.to_csv("proto.csv")

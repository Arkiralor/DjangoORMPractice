from .models import *
from .serializers import *
import pandas as pd


def get_additional(id: int):
    '''
    Stand-alone function to get additional information about a pokemon
    via its Pokedex_ID:
    '''
    stat_query = Stat.objects.get(pokedex_id=id)
    mult_query = Multiplier.objects.get(pokedex_id=id)

    stat_serialized = StatSerializer(stat_query)
    mult_serialized = MultiplierSerializer(mult_query)

    return {**stat_serialized.data, **mult_serialized.data}


def clean_df(data: pd.DataFrame) -> pd.DataFrame:
    '''
    Function to clean a dataframe by replacing NaN values with 0.
    '''
    cols = list(data.columns)
    for col in cols:
        data[f"{col}"].fillna(0, inplace=True)

    return data

def clean_dict(data: dict) -> dict:
    '''
    Function to clean fields in dictionary.
    '''
    if "id" in data.keys():
            del data["id"]
    if "type_2" in data.keys() and data["type_2"] == "0":
        data["type_2"] = "Not Available//Not Applicable"

    return data

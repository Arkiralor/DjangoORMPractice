from django.db.models import query
from rest_framework import status
from .models import Pokemon, Stat, Multiplier
from .serializers import FileUploadSerializer, MultiplierSerializer, PokemonSerializer, StatSerializer
from rest_framework import generics
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from ast import literal_eval
from .utils import clean_df, get_additional, clean_dict

# Create your views here.


class UploadFileView(generics.CreateAPIView):
    '''
    View used to upload Pokemon from a .CSV file.
    '''
    serializer_class = FileUploadSerializer

    def post(self, request):
        '''
        Uses the POST HTTP request method.
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data['file']
        dataframe_pre = pd.read_csv(file)
        dataframe = clean_df(dataframe_pre)

        rows = dataframe.to_dict(orient='records')
        for row in rows:
            row['abilities'] = literal_eval(row['abilities'])
            pokeserialized = PokemonSerializer(data=row)
            if pokeserialized.is_valid():
                pokeserialized.save()

            statserialized = StatSerializer(data=row)
            multserialized = MultiplierSerializer(data=row)

            if statserialized.is_valid() and multserialized.is_valid():
                statserialized.save()
                multserialized.save()
        return Response(
            {"Status": "File Successfully Ingested"},
            status.HTTP_201_CREATED
        )


class PokemonAPIView(APIView):
    '''
    View to retun details of all pokemon, retrieved via pokedex id.
    '''

    def get(self, request):
        '''
        Uses HTTP GET request to retrieve all pokemon.
        '''
        queryset = Pokemon.objects.all()
        pokes = PokemonSerializer(queryset, many=True)
        return Response(
            pokes.data,
            status=status.HTTP_302_FOUND
        )


class PokemonFullView(APIView):
    '''
    Class to view/edit/delete full individual pokemon data.
    '''

    def get(self, request, id: int):
        '''
        Method to get individual pokemon data.
        '''
        try:
            queryset = Pokemon.objects.get(pokedex_id=id)
            pokemon = PokemonSerializer(queryset)

        except Pokemon.DoesNotExist:
            return Response(
                {
                    "status": f"Pokemon with Pokedex #{id} does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        full_details = get_additional(id=id)
        if full_details:
            pass
        else:
            return Response(
                {
                "error": "error getting additional stats."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        result_data = {**pokemon.data, **full_details}
        result_data = clean_dict(result_data)
        

        return Response(
            result_data,
            status=status.HTTP_302_FOUND
        )

        # ## --------------------------------------------------------------------------------
        '''
        Alternate method:
        '''
        # query_1 = Stat.objects.select_related('pokedex_id').get(pokedex_id=id)
        # # print(query_1.query)
        # query_2 = Multiplier.objects.select_related('pokedex_id').get(pokedex_id=id)
        # # print(query_2.query)
        # stats = StatSerializer(query_1)
        # mults = MultiplierSerializer(query_2)

        # joined_data = { **stats.data, **mults.data}
        # del joined_data["id"]

        # return Response(
        #     joined_data,
        #     status=status.HTTP_302_FOUND
        # )

        ## --------------------------------------------------------------------------------
        '''
        Another Alternate method:
        '''
        # queryset = Stat.objects.select_related('pokedex_id').get(pokedex_id = id)
        # stats = StatSerializer(queryset)
        # # pokemon = queryset.Pokemon
        # # del stats.data["id"]

        # return Response(
        # #    {**pokemon.data, **stats.data},
        #     stats.data,
        #     status=status.HTTP_302_FOUND
        # )


class PokemonIndView(APIView):
    '''
    Class to get short summary of individual pokemon.
    '''
    def get(self, request, id: int):
        '''
        GET short summary of individual pokemon.
        '''
        try:
            queryset = Pokemon.objects.get(pokedex_id=id)
        except Pokemon.DoesNotExist:
            return Response(
                {
                    "error": f"Pokemon with Pokedex #{id} not in records."
                },
                status=status.HTTP_204_NO_CONTENT
            )

        pokemon_serialized = PokemonSerializer(queryset)

        return Response(
            pokemon_serialized.data,
            status=status.HTTP_302_FOUND
        )

        


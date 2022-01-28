from rest_framework import status
from .models import Pokemon, Stat, Multiplier
from .serializers import FileUploadSerializer, MultiplierSerializer, PokemonSerializer, StatSerializer
from rest_framework import generics
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
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
            status=status.HTTP_201_CREATED
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


class PokemonIndView(APIView):
    '''
    Class to get short summary of individual pokemon.
    '''
    def get(self, request, id: int, choice: str):
        '''
        GET short summary of individual pokemon.
        '''
        if choice == 'basic':
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
        elif choice == 'stats':
            try:
                queryset = Stat.objects.get(pokedex_id=id)
            except Stat.DoesNotExist:
                return Response(
                    {
                        "error": f"Pokemon with Pokedex #{id} not in records."
                    },
                    status=status.HTTP_204_NO_CONTENT
                )

            stats_serialized = StatSerializer(queryset)

            return Response(
                stats_serialized.data,
                status=status.HTTP_302_FOUND
            )
        elif choice == 'mults':
            try:
                queryset = Multiplier.objects.get(pokedex_id=id)
            except Multiplier.DoesNotExist:
                return Response(
                    {
                        "error": f"Pokemon with Pokedex #{id} not in records."
                    },
                    status=status.HTTP_204_NO_CONTENT
                )

            mults_serialized = MultiplierSerializer(queryset)

            return Response(
                mults_serialized.data,
                status=status.HTTP_302_FOUND
            )
        else:
            return Response(
                    {
                        "error": f"Invalid value of choice: '{choice}' in URL. Valid Options: 'basic', 'stats', 'mults'."
                    },
                    status=status.HTTP_204_NO_CONTENT
                )


        


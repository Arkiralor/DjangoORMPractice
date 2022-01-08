from rest_framework import status
from .models import Pokemon, Stat, Multiplier
from .serializers import FileUploadSerializer, MultiplierSerializer, PokemonSerializer, StatSerializer
from rest_framework import generics
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from ast import literal_eval
from .utils import get_additional
import json

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
        dataframe = pd.read_csv(file)

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


class PokemonIndView(APIView):
    '''
    Class to view/edit/delete individual pokemon data.
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
            print(full_details)
        else:
            full_details = {
                "error": "error getting additional stats."
            }
            return Response(
                full_details,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # result_data = json.dumps({**pokemon.data, **full_details})
        result_data = {**pokemon.data, **full_details}

        return Response(
                result_data,
                status=status.HTTP_302_FOUND
            )
        
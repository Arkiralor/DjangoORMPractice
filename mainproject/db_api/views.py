from rest_framework import status
from .models import Pokemon, Stats, Multipliers
from .serializers import FileUploadSerializer, MultiplierSerializer, PokemonSerializer, StatSerializer
from rest_framework import generics
import io
import csv
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from ast import literal_eval

# Create your views here.


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request):
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
            statserialized.is_valid(raise_exception=True)
            multserialized = MultiplierSerializer(data=row)
            multserialized.is_valid(raise_exception=True)

            if statserialized.is_valid() and multserialized.is_valid():
                statserialized.save()
                multserialized.save()
        return Response(
            {"Status": "File Successfully Ingested"},
            status.HTTP_201_CREATED
            )

class PokemonAPIView(APIView):

    def get(self, request):
        queryset = Stats.objects.all()
        pokes = PokemonSerializer(queryset, many=True)
        print(pokes)
        return Response(
            pokes.data,
            status=status.HTTP_302_FOUND
        )

from django.urls import path
from .views import PokemonAPIView, PokemonFullView, PokemonIndView, UploadFileView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='batch_upload'),
    path('pokemon/', PokemonAPIView.as_view(), name='retrieve_all'),
    path('pokemon/<int:id>', PokemonIndView.as_view(), name='individual_pokemon'),
    path('pokemon/<int:id>/full', PokemonFullView.as_view(),
         name='individual_pokemon_full')
]

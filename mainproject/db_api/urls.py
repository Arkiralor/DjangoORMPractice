from django.urls import path
from .views import PokemonAPIView, UploadFileView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='batch_upload'),
    path('pokemon/', PokemonAPIView.as_view(), name='retrieve_all')
]

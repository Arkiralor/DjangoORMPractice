from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentView.as_view(), name='all_students'),
    path('student/<int:id>', StudentIndView.as_view(), name='student')
   
]
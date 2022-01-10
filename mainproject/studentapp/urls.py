from django.urls import path
from .views import *

urlpatterns = [
    path('student/all', StudentView.as_view(), name='all_students'),
   
]
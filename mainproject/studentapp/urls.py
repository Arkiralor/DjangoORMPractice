from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentView.as_view(), name='all_students'),
    path('student/<int:id>', StudentIndView.as_view(), name='student'),
    path('academicstaff/',
         AcademianView.as_view(
             {
                 'get': 'list', 
                 'post': 'create'
                 }
            ), 
                 name='academic_staff'
        ),
    path('academicstaff/<int:id>', AcademianIndView.as_view(
                {
                    'get': 'retrieve', 
                    'put': 'update', 
                    'delete': 'destroy'
                }
            ), 
            name='individual_academic_staff'
        )
]

from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class StudentView(APIView):
    '''
    View for all students.
    '''

    def get(self, request):
        '''
        GET list of all students.
        '''
        queryset = Student.objects.all()
        students = StudentSerializer(data=queryset, many=True)
        print(students.initial_data)

        if students.is_valid():
            return Response(
                students.data,
                status=status.HTTP_302_FOUND
            )
        else:
            return Response(
                {
                    "error": "NOT FOUND"
                },
                status=status.HTTP_404_NOT_FOUND
            )



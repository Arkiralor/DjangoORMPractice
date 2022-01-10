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
        students = StudentSerializer(queryset, many=True)
        return Response(
                students.data,
                status=status.HTTP_302_FOUND
            )
    
    def post(self, request):
        serialized = StudentSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentIndView(APIView):
    '''
    View for all students.
    '''

    def get(self, request, id:int):
        '''
        GET list of all students.
        '''
        try:
            queryset = Student.objects.get(pk=id)
            student = StudentSerializer(queryset)
        except Student.DoesNotExist:
            return Response(
                    {
                        "error":"student not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(
                    student.data,
                    status=status.HTTP_302_FOUND
                )

    




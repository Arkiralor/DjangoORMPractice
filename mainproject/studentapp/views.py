from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

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
        '''
        POST/add a new student.
        '''
        serialized = StudentSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentIndView(APIView):
    '''
    View for individual students.
    '''

    def get(self, request, id: int):
        '''
        GET individual students via id.
        '''
        try:
            queryset = Student.objects.get(pk=id)
            student = StudentSerializer(queryset)
        except Student.DoesNotExist:
            return Response(
                {
                    "error": "student not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            student.data,
            status=status.HTTP_302_FOUND
        )

    def put(self, request, id: int):
        '''
        PUT/PATCH an individual student.
        '''
        try:
            queryset = Student.objects.get(pk=id)
            serialized = StudentSerializer(queryset, data=request.data)
        except Exception as err:
            return Response(
                {
                    "error": str(err)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if serialized.is_valid():
            serialized.save()
            return Response(
                serialized.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": str(serialized.errors)
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )

    def delete(self, request, id: int):
        '''
        Delete an individual student.
        '''
        try:
            queryset = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            return Response(
                {
                    "error": f"student with id = {id} does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serialized_student = StudentSerializer(queryset)
        queryset.delete()
        return Response(
            serialized_student.data,
            status=status.HTTP_410_GONE
        )

class AcademianView(ModelViewSet):
    '''
    API View for all academians.
    '''
    queryset = Academian.objects.all()
    serializer_class = AcademinSerializer

class AcademianIndView(ModelViewSet):
    '''
    API View for individual academians.
    '''
    queryset = Academian.objects.get(id)
    serializer_class = AcademinSerializer
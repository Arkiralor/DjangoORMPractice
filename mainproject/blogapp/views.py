from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class UserView(ModelViewSet):
    '''
    API Model View for all blog posts.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class BlogPostView(ModelViewSet):
    '''
    API Model View for all blog posts.
    '''
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'
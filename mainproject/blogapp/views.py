from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated


# Create your views here.

class UserView(ModelViewSet):
    '''
    API Model View for all blog posts.
    '''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

# class BlogPostView(ModelViewSet):
#     '''
#     API Model View for all blog posts.
#     '''
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_field = 'id'

class BlogView(APIView):
    '''
    View to get all blog-posts and post new blog-post.
    '''

    def get(self, request):
        try:
            queryset = Blog.objects.all()
            blog_posts = BlogSerializer(queryset, many=True)
        except Blog.DoesNotExist:
            return Response(
                {
                    "error": "No posts in database."
                },
                status=status.HTTP_204_NO_CONTENT
            )

        return Response(
            blog_posts.data,
            status=status.HTTP_302_FOUND
        )

    def post(self, request):
        try:
            data = BlogSerializer(data=request.data)
        except Exception as err:
            return Response(
                {
                    "error": str(err)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if data.is_valid():
            data.save()
            return Response(
                data.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "error": str(data.errors)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class BlogPostView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

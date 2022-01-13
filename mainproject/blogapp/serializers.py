from rest_framework import serializers
from .models import User, Blog

# Define your serializers here:

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'date_created']

class BlogSerializer(serializers.ModelSerializer):
    authored_by = UserSerializer(read_only = True)

    class Meta:
        model = Blog
        fields = ['title', 'body', 'date_created', 'authored_by']
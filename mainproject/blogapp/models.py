from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title +' by '+self.author.username

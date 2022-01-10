from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class Academian(models.Model):
    fname = models.CharField(max_length=16)
    mname = models.CharField(max_length=16, null=True, blank=True)
    lname = models.CharField(max_length=16)
    date_of_birth = models.DateField(default='1992-01-01')
class Faculty(models.Model):
    type = models.CharField(max_length=16)
    dean = models.ForeignKey(Academian, on_delete=SET_NULL)
class Department(models.Model):
    name = models.CharField(max_length=64)
    faculty = models.ForeignKey(Faculty, on_delete=CASCADE)

class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    fname = models.CharField(max_length=16)
    mname = models.CharField(max_length=16, null=True, blank=True)
    lname = models.CharField(max_length=16)
    date_of_birth = models.DateField(default='1992-01-01')
    degree = models.CharField(max_length=32)


    def __str__(self):
        return self.fname + ' ' + self.lname
        
class Schedule(models.Model):

    
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class Academian(models.Model):
    fname = models.CharField(max_length=16)
    mname = models.CharField(max_length=16, null=True, blank=True)
    lname = models.CharField(max_length=16)
    date_of_birth = models.DateField(default='1992-01-01')
    RANK_CHOICES = (
        ('Prof.','Professor'),
        ('Asst. Prof.','Assistant Professor'),
        ('Asc. Prof.','Associate Professor'),
        ('Lec.','Lecturer')
    )
    rank = models.CharField(max_length=64, choices=RANK_CHOICES)
    date_of_joining = models.DateField(default='2017-01-01')

    def __str__(self):
        return self.rank + ' ' + self.fname + ' ' + self.lname


class Faculty(models.Model):
    type = models.CharField(max_length=16)
    dean = models.ForeignKey(Academian, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"Faculty of {self.type}"


class Department(models.Model):
    name = models.CharField(max_length=64)
    faculty = models.ForeignKey(Faculty, on_delete=CASCADE)
    head = models.ForeignKey(Academian, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"Department of {self.name}"

class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    fname = models.CharField(max_length=16)
    mname = models.CharField(max_length=16, null=True, blank=True)
    lname = models.CharField(max_length=16)
    date_of_birth = models.DateField(default='1992-01-01')
    degree = models.CharField(max_length=32)
    major = models.ForeignKey(Department, on_delete=CASCADE)

    def __str__(self):
        return self.fname + ' ' + self.lname
        
class Payroll(models.Model):
    staff = models.ForeignKey(Academian, on_delete=CASCADE)
    basic_pay = models.IntegerField()
    conveyance_allowance = models.IntegerField()
    house_rent_allowance = models.IntegerField()
    medical_allowance = models.IntegerField()
    special_allowance = models.IntegerField()
    tax_deduction = models.DecimalField(decimal_places=2, max_digits=16)
    pf_deduction = models.DecimalField(decimal_places=2, max_digits=16)
    medical_insurance = models.IntegerField()
    take_home = models.DecimalField(decimal_places=2, max_digits=16)

    def __str__(self):
        return f"{self.staff}"

class ScholarshipScheme(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    grant_body = models.CharField(max_length=256)
    grant_body_url = models.URLField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    student = models.ForeignKey(Student, on_delete=CASCADE)
    scheme = models.ForeignKey(ScholarshipScheme, on_delete=CASCADE)
    amount = models.IntegerField()
    PERIOD_CHOICES = (
        ('Monthly', 'monthly'),
        ('Quarterly', 'quarterly'),
        ('Bi-Annually', 'biannually'),
        ('Annually', 'annually')
    )
    period = models.CharField(max_length=32, choices=PERIOD_CHOICES)

    def __str__(self):
        return f"{self.student}, {self.scheme}"
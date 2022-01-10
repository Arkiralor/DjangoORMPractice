from rest_framework import serializers
from .models import Academian, Faculty, Department, Student, Payroll, ScholarshipScheme, Scholarship

# Create your serializers here:

class AcademinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academian
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'


class ScholarshipSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipScheme
        fields = '__all__'


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = '__all__'

from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('academicstaff', AcademianView)
router.register('faculty', FacultyView)
router.register('department', DepartmentView)
router.register('degree', DegreeView)
router.register('payroll', PayrollView)
router.register('scholarshipscheme', ScholarshipSchemeView)
router.register('scholarship', ScholarshipView)


urlpatterns = [
    path('student/', StudentView.as_view(), name='all_students'),
    path('student/<int:id>', StudentIndView.as_view(), name='student'),
    path('department/alt/<int:id>', DepartmentAltView.as_view(), name='department_alt'),
    path('', include(router.urls))
]
## Unused urls.py snippet:
# path('academicstaff/',
    #      AcademianView.as_view(
    #          {
    #              'get': 'list', 
    #              'post': 'create',
    #              'put': 'update',
    #              'delete': 'destroy'
    #              }
    #         ), 
    #              name='academic_staff'
    #     ),

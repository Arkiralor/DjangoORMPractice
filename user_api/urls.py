from django.urls import path
from .views import GetUserView, AddUserView, UserLoginView, UserLogoutView

# Include your URLs here:

urlpatterns = [
    path('all/', GetUserView.as_view(), name='all_users'),          # Get
    path('new/', AddUserView.as_view(), name='add_user'),           # Post
    path('login/', UserLoginView.as_view(), name='login'),          # Post
    path('logout/', UserLogoutView.as_view(), name='logout'),       # Get
]
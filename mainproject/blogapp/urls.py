from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView, BlogPostView

router = DefaultRouter()
router.register('users', UserView)
router.register('blog/posts', BlogPostView)


urlpatterns = [
    path('blog/', include(router.urls))
]
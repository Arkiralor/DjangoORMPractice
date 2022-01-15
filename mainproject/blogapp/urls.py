from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView, BlogView, BlogPostView

router = DefaultRouter()
router.register('blog/users', UserView)
# router.register('posts', BlogPostView)
# router.register('posts', BlogView.as_view({"get": "list","post": "create"}), basename='blog_posts')
# router.register('posts', BlogView.as_view(), basename='blog_posts')


urlpatterns = [
    path('', include(router.urls)),
    path('blog/posts', BlogView.as_view(), name='blog_posts'),
    path('blog/posts/<int:id>', BlogPostView.as_view(), name='ind_blog_posts')
]
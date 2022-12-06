from django.urls import path
from .views import posts_view, like_post

app_name = 'posts'

urlpatterns = [
    path('', posts_view, name='post-list'),
    path('like/', like_post, name='like_post'),
]

from django.urls import path
from .views import all_blog_posts

urlpatterns = [
    path('', all_blog_posts, name='all_blog_posts'),
]

handler404 = 'noble_candles.view.handler404'

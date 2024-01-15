from django.urls import path
from .views import all_blog_posts, blogpost_details

urlpatterns = [
    path('', all_blog_posts, name='all_blogposts'),
    path('<int:blogpost_id>/', blogpost_details, name='blogpost_details'),
]

handler404 = 'noble_candles.view.handler404'

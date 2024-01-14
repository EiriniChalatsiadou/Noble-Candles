from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.db.models import Q
from .models import BlogPost


def all_blog_posts(request):

    published_blogposts = BlogPost.objects.get_published_blogposts()

    context = {
        'published_blogposts': published_blogposts,
    }
    return render(request, 'blog/blogposts_list.html', context)
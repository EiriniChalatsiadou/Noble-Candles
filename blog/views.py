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


def blogpost_details(request, blogpost_id):

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    # Check if the blog post is published
    if not blogpost.published:
        # show 404 if unpublished
        return render(request, '404.html')

    context = {
        'blogpost': blogpost,
    }
    return render(request, 'blog/blogpost_details.html', context)
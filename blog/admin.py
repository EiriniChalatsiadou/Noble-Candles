from django.contrib import admin
from .models import BlogPost


class BlogPostMessageAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'date_updated', 'title',
                    'content', 'published', 'image_url', 'author')
    ordering = ('date_created',)


# Register your models here.
admin.site.register(BlogPost, BlogPostMessageAdmin)

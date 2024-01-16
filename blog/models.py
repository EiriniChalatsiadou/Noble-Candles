from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPostManager(models.Manager):
    def get_published_blogposts(self):
        return self.filter(published=True).order_by('-date_updated')


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = BlogPostManager()

    def __str__(self):
        return self.title

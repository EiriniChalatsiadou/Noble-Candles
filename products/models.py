from django.db import models
from reviews.models import Review


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def _str_(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_number = models.IntegerField(default=0)

    @property
    def rating(self):
        # Calculate the average rating for the product
        average_rating = Review.objects.filter(product=self).aggregate(avg_rating=models.Avg('rating'))['avg_rating']
        return round(average_rating, 1) if average_rating else None

    def in_stock(self):
        return self.stock_number > 0

    def __str__(self):
        return self.name

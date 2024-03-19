from django.db import models
from products.models import Product
from profiles.models import UserProfile
from profanity.validators import validate_is_profane

class RatingEnum(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5, '5'


class Review(models.Model):
    """ A review model for users to review products """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingEnum.choices, default=RatingEnum.ONE)
    content = models.TextField(max_length=1024, validators=[validate_is_profane])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.user.username if self.user else ''
        return f"Review by {username} for {self.product.name}"

def review_exists_for_product(product, user_profile):
    return  Review.objects.all().filter(product=product).filter(user=user_profile.id).exists()
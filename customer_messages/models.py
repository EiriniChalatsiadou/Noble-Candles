from django.db import models

class CustomerMessage(models.Model):
    """
    Model to store customer messages.
    """

    date_received = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.email}"

    class Meta:
        verbose_name_plural = "Customer Messages"
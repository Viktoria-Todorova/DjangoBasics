from django.db import models

from destinations.models import Destination


# Create your models here.

class Review(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE ,related_name='reviews')
    is_published = models.BooleanField(default=True)

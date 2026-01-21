from django.db import models

from common.models import TimeStampedModel


# Create your models here.
class Review(TimeStampedModel):
    author = models.CharField(max_length=100)
    body=models.TextField()
    rating = models.DecimalField(decimal_places=2, max_digits=4)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    is_spoiler = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
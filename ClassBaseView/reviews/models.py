from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from destinations.models import Destination
from travelers.models import Traveler


# Create your models here.

class Review(models.Model):
    class ReviewTypeChoices(models.TextChoices):
        TEXT = "TEXT", "Text"
        VIDEO = "VIDEO", "Video"
        AUDIO = "AUDIO", "Audio"

    body = models.TextField()

    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    is_verified = models.BooleanField(default=False)
    review_type = models.CharField(max_length=10, choices=ReviewTypeChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name="reviews")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="reviews")

    def clean(self) -> None:
        if self.destination_id and not self.destination.is_available:
            raise ValidationError("Cannot create a review with a destination that has not been available")

    def __str__(self):
        return f"{self.traveler} - {self.destination}"

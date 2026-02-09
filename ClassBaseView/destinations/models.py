from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from common.choices import CountryChoices
from travelers.models import Traveler


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=10, choices=CountryChoices.choices)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    travelers = models.ManyToManyField(Traveler, related_name="destinations", blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'country'],
                name="unique_destination_name_per_country"
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name} {self.country}")
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
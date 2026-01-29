from django.db import models
from django.utils.text import slugify

from common.models import TimeStampedModel


# Create your models here.
class Book(TimeStampedModel):
    class GenreChoices(models.TextChoices):
        FICTION = 'Fiction','Fiction'
        NON_FICTION = 'Non-Fiction','Non-Fiction'
        FANTASY = 'Fantasy','Fantasy'
        SCIENCE = 'Science','Science'
        HISTORY = 'History','History'
        MYSTERY = 'Mystery','Mystery'

    title = models.CharField(max_length=100,unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(choices=GenreChoices.choices,max_length=50)
    publishing_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(max_length=100,blank=True,unique=True)
    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    publisher = models.CharField(
        max_length=100,
    )
    tags = models.ManyToManyField("Tag")
    def save(self,*args,**kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.publisher}")

        super().save(*args,**kwargs)




class Tag(models.Model):
    name = models.CharField(max_length=50)
    books= models.ManyToManyField(Book)

    def __str__(self) ->str:
        return self.name
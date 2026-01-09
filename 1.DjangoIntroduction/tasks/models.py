from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title} - {self.text} - is completed: {self.is_complete}"
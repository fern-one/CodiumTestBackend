from unicodedata import name
from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

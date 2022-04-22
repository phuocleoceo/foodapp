from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="photos/categories", blank=True)

    def __str__(self):
        return self.name

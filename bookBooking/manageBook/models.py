from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    publish_date = models.DateField()
    categories = models.ManyToManyField("manageBook.Category")
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

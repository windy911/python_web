from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    pages = models.IntegerField(default=0)
    series = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=50)
    books = models.IntegerField(default=0)
    def __str__(self):
        return self.name
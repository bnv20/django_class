# data/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    published_date = models.DateTimeField()
    keyword = models.CharField(max_length=100)

    def __str__(self):
        return self.title


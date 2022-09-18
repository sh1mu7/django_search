from email.quoprimime import quote
from unicodedata import name
from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author

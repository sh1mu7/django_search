from email.quoprimime import quote
from unicodedata import name
from django.db import models
from django.urls import reverse


class Quote(models.Model):
    quote = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.author


# class Posts(models.Model):
#     DIVISION_CHOICES = [
#         ('Rajshahi', 'Rajshahi'),
#         ("Dhaka", 'Dhaka'),
#         ('Khulna', 'Khulna')
#     ]
#     DISTRICT_CHOICES = [
#         ('CHP', 'CHP'),
#         ('RAJ','Raj'),
#         ('KIS','KIS'),
#         ('SAT', 'SAT'),
#         ('PAK', 'PAK'),
#
#     ]
#     SOLID_CANCER = [
#         ('YES', 'YES'),
#         ('NO', 'NO')
#     ]
#     FINANCE_CHOICES = [
#         ('Good', 'Good'),
#         ('Rich', 'Rich'),
#         ('Poor', 'Poor'),
#     ]
#     name = models.CharField(max_length=30)
#     division = models.CharField(max_length=50, choices=DIVISION_CHOICES)
#     district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
#     thana = models.CharField(max_length=20)
#     solid_cancer = models.CharField(max_length=3, choices=SOLID_CANCER)
#     age = models.IntegerField()
#     finance = models.CharField(max_length=4, choices=FINANCE_CHOICES)
#
#     def __str__(self):
#         return self.name


class Posts(models.Model):
    author_name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    post = models.TextField()
    published_date = models.DateField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.author_name

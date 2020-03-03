from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    birth_date = models.DateField()
    position = models.CharField(max_length=60)

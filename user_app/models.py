from django.db import models

class UserData(models.Model):
    full_name = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)
    salary = models.IntegerField()
    country = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=200)

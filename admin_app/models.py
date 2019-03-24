from django.db import models

class Admin(models.Model):
    admin_email = models.CharField(max_length=200)
    admin_password = models.CharField(max_length=200)

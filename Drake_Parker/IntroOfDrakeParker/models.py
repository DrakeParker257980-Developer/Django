from django.db import models

# Create your models here.

class User(models.Model):
    users_id = models.AutoField
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Joined_On = models.DateField()
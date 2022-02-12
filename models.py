from django.db import models

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_name = models.CharField(max_length=25)
    user_password = models.CharField(max_length=25)
    number = models.IntegerField()
    email = models.EmailField(max_length=50)

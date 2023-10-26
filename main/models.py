from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    revenue = models.BigIntegerField()

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.BigIntegerField()

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_ROLES = (
        ('member', 'Member'),
        ('employee', 'Employee'),
        ('writer', 'Writer'),
    )

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    revenue = models.BigIntegerField()
    role = models.CharField(max_length=10, choices=USER_ROLES)

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.BigIntegerField()
    role = models.CharField(max_length=10, choices=USER_ROLES)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)




from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    revenue = models.BigIntegerField(default=0)
    role = models.CharField(max_length=20, default='Writer')

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.BigIntegerField(default=100000)
    role = models.CharField(max_length=20, default='Member')
    buku_dibeli = models.ManyToManyField(Book, blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default='Employee')




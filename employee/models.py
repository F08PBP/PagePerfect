from django.db import models
from book.models import Book

# Create your models here.

class Catalog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isShowToMember = models.BooleanField(default=False)
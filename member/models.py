from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.
class Keranjang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=0)
    total_harga = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + " " + str(self.book)
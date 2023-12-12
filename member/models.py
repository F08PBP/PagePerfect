from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from main.models import Member
# Create your models here.
class BukuOrder(models.Model):
    book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)

class Order(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    buku = models.ManyToManyField(BukuOrder)

    def get_keranjang_books(self):
        return self.buku.all()
    
    def get_keranjang_total(self):
        total = 0
        for buku in self.buku.all():
            total += buku.book.harga
        return total
    
class CartItem(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class BoughtItem(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    cart = models.ManyToManyField(CartItem)
    notes = models.TextField(null=True, blank=True)

class PurchasedItem(models.Model):
    bought_item = models.ForeignKey(BoughtItem, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
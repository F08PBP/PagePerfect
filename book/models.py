from django.db import models

# Create your models here.

class Book(models.Model):
    STATUS_CHOICES = [
        ("ACCEPT", 'Accept'),
        ("WAITING", 'Waiting'),
        ("DENIED", 'Denied'),
        ("NO STATUS", 'No Status'),
    ]
    bookID = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    isbn = models.TextField(null=True, blank=True)
    isbn13 = models.BigIntegerField(null=True, blank=True)
    language_code = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    text_reviews_count = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
    harga = models.IntegerField(null=True, blank=True)
    jumlah_buku = models.IntegerField(null=True, blank=True)
    jumlah_terjual = models.IntegerField(default=0, blank=True)
    statusAccept = models.CharField(max_length=10, choices=STATUS_CHOICES, default="NO STATUS")
    isInCatalog = models.BooleanField(default=False)
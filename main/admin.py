from django.contrib import admin
from main.models import Author, Member, Employee
from book.models import Book

# Register your models here.

admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Employee)
admin.site.register(Book)

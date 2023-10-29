from django.contrib import admin
from .models import Author, Member, Employee


# Register your models here.
admin.site.register(Author)
admin.site.register(Member)
admin.site.register(Employee)

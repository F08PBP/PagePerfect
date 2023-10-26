from django.urls import path
from .views import main, catalogBook, bookFromWriter

app_name = 'employee'

urlpatterns = [
    path('', main, name='main'),
    path('catalog', catalogBook, name='catalogBook'),
    path('acc', bookFromWriter, name='bookFromWriter')
]

from django.contrib import admin
from django.urls import path, include
from member.views import show_main, logout_user, get_books_json, show_books_bought, add_message, get_money, add_money, shopping_cart
app_name = 'member'

urlpatterns = [
    path('main/', show_main, name='show_main'),
    path('logout/', logout_user, name='logout_user'),
    path('show_books/', get_books_json, name="show_books"),
    path('show_books_bought/', show_books_bought, name="show_books_bought"),
    path('add_message/', add_message, name='add_message'),,
    path('get_money/', get_money, name='get_money'),
    path('add_money/', add_money, name='add_money'),
    path('shopping_cart/', shopping_cart, name='shopping_cart' )
    ]
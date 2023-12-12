from django.contrib import admin
from django.urls import path, include
from book.views import get_books
from member.views import add_book_to_cart, add_book_to_cart_flutter, confirm_purchase, confirm_purchase_flutter, delete_cart, edit_cart, get_books_for_json, get_cart, show_cart_json, show_main, logout_user, get_books_json, show_books_bought, get_money, add_money, shopping_cart, show_purchased_item, show_transaction
app_name = 'member'

urlpatterns = [
    path('main/', show_main, name='show_main'),
    path('logout/', logout_user, name='logout_user'),
    path('show_books/', get_books_json, name="show_books"),
    path('show_books_bought/', show_books_bought, name="show_books_bought"),
    path('get_money/', get_money, name='get_money'),
    path('add_money/', add_money, name='add_money'),
    path('shopping_cart/', shopping_cart, name='shopping_cart' ),
    path('add_book_to_cart/', add_book_to_cart, name='add_book_to_cart'),
    path('add_book_to_cart_flutter/', add_book_to_cart_flutter, name='add_book_to_cart_flutter'),
    path('edit-cart/', edit_cart, name='edit_cart'),
    path('get-cart/', get_cart, name='get_cart'),
    path('delete-cart/<str:title>/', delete_cart, name='delete_cart'),
    path('confirm_purchase/', confirm_purchase, name='confirm_purchase'),
    path('confirm_purchase_flutter/', confirm_purchase_flutter, name='confirm_purchase_flutter'),
    path('get-book/', get_books, name='get_books'),
    path('show-transaction/', show_transaction, name='show_transaction'),
    path('show-cart-json/', show_cart_json, name='show_cart_json'),
    path('get-book-json/', get_books_for_json, name='get_books_for_json'),
    path('show-purchased-json/<int:id>/', show_purchased_item, name='show_purchased_item'),
]
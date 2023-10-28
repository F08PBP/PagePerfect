from django.contrib import admin
from django.urls import path, include
from member.views import show_main, logout_user, get_books_json

app_name = 'member'

urlpatterns = [
    path('main/', show_main, name='show_main'),
    path('logout/', logout_user, name='logout_user'),
    path('show_books/', get_books_json, name="show_books")
    ]
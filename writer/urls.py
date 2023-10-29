from django.urls import path
from . import views

app_main = 'writer'

urlpatterns = [
    path('get-product/', views.get_book_json, name="get_book_json"),
    path('create-product-ajax/', views.add_book_ajax, name="add_book_ajax"),
    path('show-collection/', views.show_collection, name="show_collection"),
    path('show-status-book/', views.show_status_book, name="show_status_book"),
    path('show-revenue/', views.show_revenue, name="show_revenue")
]
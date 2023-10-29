from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib import messages  
from django.http import HttpResponse, HttpResponseNotFound
from book.models import Book
from django.core import serializers
# Create your views here.

@csrf_exempt
def add_book_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        harga = request.POST.get("harga")
        jumlah_buku = request.POST.get("jumlah_buku")
        
        new_book = Book(title=title, authors=request.user.username, harga=harga, jumlah_buku=jumlah_buku, statusAccept='WAITING')
        new_book.save()
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound


def get_book_json(request):
    books_item = Book.objects.all().filter(authors=request.user.username)
    return HttpResponse(serializers.serialize('json', books_item))


def get_acc_book_json(request):
    acc_books_item = Book.objects.all().filter(authors=request.user.username).filter(statusAccept='ACCEPT')
    return HttpResponse(serializers.serialize('json', acc_books_item))


def get_waiting_book_json(request):
    waiting_books_item = Book.objects.all().filter(authors=request.user.username).filter(statusAccept='WAITING')
    return HttpResponse(serializers.serialize('json', waiting_books_item))


def get_denied_book_json(request):
    denied_books_item = Book.objects.all().filter(authors=request.user.username).filter(statusAccept='DENIED')
    return HttpResponse(serializers.serialize('json', denied_books_item))


def show_collection(request):
    context = {
        'name' : request.user.username,
    }
    return render(request, 'show_collection.html', context)


def show_status_book(request):
    context = {
        'name' : request.user.username,
    }
    return render(request, 'show_status_book.html', context)


def show_revenue(request):
    books_item = Book.objects.all().filter(authors=request.user.username)
    total_revenue = 0
    for book in books_item:
        total_revenue += book.harga * book.jumlah_terjual
    context = {
        'name' : request.user.username,
        'total_revenue' : total_revenue
    }
    return render(request, 'show_revenue.html', context)
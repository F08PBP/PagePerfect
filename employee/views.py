from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


#@login_required(login_url='login')
def main(request):
    response = {}
    return render(request, 'catalog.html', response)

def mainBook(request, book_id):
    response = {"book_id" : book_id}
    return render(request, 'book.html', response)

def mainSetBook(request):
    response = {}
    return render(request, 'setBook.html', response)

def mainBookFromWriter(request):
    response = {}
    return render(request, 'bookFromWriter.html', response)

def accBookFromWriter(request):
    if request.method == 'POST' :
        book_id = request.POST.get('book_id')
        try:
            instance = Book.objects.get(bookID=book_id)
            instance.statusAccept = "ACCEPT"
            instance.save()
            return HttpResponse({'status': 'The book ' + instance.title + ' was accepted'} , status=200)
        except Book.DoesNotExist:
            return HttpResponse({'status': 'Error: Object not found'}, status=404)
    return HttpResponse({'status': 'Error: Invalid request'}, status=400)

def denBookFromWriter(request):
    if request.method == 'POST' :
        book_id = request.POST.get('book_id')
        try:
            instance = Book.objects.get(bookID=book_id)
            instance.statusAccept = "DENIED"
            instance.save()
            return HttpResponse({'status': 'The book ' + instance.title + ' was denied'} , status=200)
        except Book.DoesNotExist:
            return HttpResponse({'status': 'Error: Object not found'}, status=404)
    return HttpResponse({'status': 'Error: Invalid request'}, status=400)

def catalogBook(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def getBook(request, book_id):
    data = Book.objects.filter(bookID = book_id).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def bookFromWriter(request):
    data = Book.objects.filter(statusAccept = "WAITING").all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def setBook(request):
    data = Book.objects.filter(statusAccept = "ACCEPT").all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def test(request):
    data = Book.objects.filter(bookID = 55).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
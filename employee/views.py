from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.http import HttpResponse
from django.core import serializers

from .models import Catalog
from main.models import Employee

import json

# Create your views here.


#@login_required(login_url='login')

@login_required(login_url='/login')
def main(request):
    try :
        employee = Employee.objects.get(user=request.user.id)
        response = {
            "name" : request.user.username
        }
        return render(request, 'employee.html', response)
    except : 
        return render(request, 'failed.html')

@login_required(login_url='/login')
def mainCatalog(request):
    try :
        employee = Employee.objects.get(user=request.user.id)
        response = {}
        return render(request, 'catalog.html', response)
    except : 
        return render(request, 'failed.html')

@login_required(login_url='/login')
def mainBook(request, book_id):
    try :
        employee = Employee.objects.get(user=request.user.id)
        response = {"book_id" : book_id}
        return render(request, 'book.html', response)
    except : 
        return render(request, 'failed.html')

@login_required(login_url='/login')
def mainSetBook(request):
    try :
        employee = Employee.objects.get(user=request.user.id)
        response = {}
        return render(request, 'setBook.html', response)
    except : 
        return render(request, 'failed.html')

@login_required(login_url='/login')
def mainBookFromWriter(request):
    try :
        employee = Employee.objects.get(user=request.user.id)
        response = {}
        return render(request, 'bookFromWriter.html', response)
    except : 
        return render(request, 'failed.html')

@login_required(login_url='/login')
def accBookFromWriter(request):
    if request.method == 'POST' :
        book_id = request.POST.get('book_id')
        try:
            instance = Book.objects.get(bookID=book_id)
            instance.statusAccept = "ACCEPT"
            instance.save()

            catalog= Catalog.objects.create(
                 book=instance,
            )
            return HttpResponse({'status': 'The book ' + instance.title + ' was accepted'} , status=200)
        except Book.DoesNotExist:
            return HttpResponse({'status': 'Error: Object not found'}, status=404)
    return HttpResponse({'status': 'Error: Invalid request'}, status=400)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def catalogBook(request):
    data = Catalog.objects.all()
    catalog_data = []
    for entry in data:
        book = Book.objects.filter(bookID = entry.book.bookID).all()
        for book_instance in book:
            catalog_data.append({
                'Catalog' : entry.pk,
                'isShow' : entry.isShowToMember,
                'bookID': book_instance.bookID,
                'title': book_instance.title,
                'authors' : book_instance.authors,
                'average_rating' : book_instance.average_rating,
                'jumlah_buku' : book_instance.jumlah_buku,
                'jumlah_terjual' : book_instance.jumlah_terjual
                # Include other fields you want to serialize
            })

    json_data = json.dumps(list(catalog_data))

    return HttpResponse(json_data, content_type="application/json")

@login_required(login_url='/login')
def showingToMember(request):
    if request.method == 'POST' :
        catalog_id = request.POST.get('catalog_id')
        try:
            instance = Catalog.objects.filter(pk= catalog_id).update(isShowToMember=True)
            return HttpResponse({'status': 'The book ' + ' was showed'} , status=200)
        except Book.DoesNotExist:
            return HttpResponse({'status': 'Error: Object not found'}, status=404)
    return HttpResponse({'status': 'Error: Invalid request'}, status=400)

@login_required(login_url='/login')
def notShowingToMember(request):
    if request.method == 'POST' :
        catalog_id = request.POST.get('catalog_id')
        try:
            instance = Catalog.objects.filter(pk= catalog_id).update(isShowToMember=False)
            return HttpResponse({'status': 'The book ' + ' was not showed'} , status=200)
        except Book.DoesNotExist:
            return HttpResponse({'status': 'Error: Object not found'}, status=404)
    return HttpResponse({'status': 'Error: Invalid request'}, status=400)

@login_required(login_url='/login')
def getBook(request, book_id):
    data = Book.objects.filter(bookID = book_id).all()
    print(data)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def bookFromWriter(request):
    data = Book.objects.filter(statusAccept = "WAITING").all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def setBook(request):
    data = Book.objects.filter(statusAccept = "ACCEPT").all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def test(request):
    data = Catalog.objects.filter(isShowToMember = True).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Tambahan buat bisa akses employee.html dari views.py di main
def employee_page(request):
    return render(request, 'employee.html')
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
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

def get_books_for_employee(request):
    books = Book.objects.filter(pk__lte=100, statusAccept ="WAITING")[:100]
    books_data = serializers.serialize('json', books)
    books_list = json.loads(books_data)
    return JsonResponse(books_list, safe=False)

def get_catalog_json(request):
    books = Book.objects.filter(pk__lte=100, statusAccept ="ACCEPT")[:100]
    books_data = serializers.serialize('json', books)
    books_list = json.loads(books_data)
    return JsonResponse(books_list, safe=False)

def get_active_json(request):
    catalog = Catalog.objects.all()
    catalog_data = serializers.serialize('json', catalog)
    catalog_list = json.loads(catalog_data)
    return JsonResponse(catalog_list, safe=False)

@csrf_exempt
def update_book_status(request, book_id, status):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        if status in [choice[0] for choice in Book.STATUS_CHOICES]:
            book.statusAccept = status
            book.save()
            return JsonResponse({'status': 'success', 'message': 'Book status updated'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid status'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

@csrf_exempt
def add_book_stock(request):
    if request.method == "POST":
        data = request.POST
        book_id = data.get('book_id')
        added_stock = int(data.get('added_stock'))

        try:
            book = Book.objects.get(pk=book_id)
            book.jumlah_buku += added_stock
            book.save()
            return JsonResponse({'status': 'success', 'new_stock': book.jumlah_buku})
        except Book.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@csrf_exempt
def toggle_catalog_visibility(request, pk):
    if request.method == 'POST':
        try:
            catalog_entry = Catalog.objects.get(pk=pk)
            catalog_entry.isShowToMember = not catalog_entry.isShowToMember
            catalog_entry.save()
            return JsonResponse({'success': True, 'isShowToMember': catalog_entry.isShowToMember})
        except Catalog.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Catalog not found'}, status=404)
    else:
        return HttpResponseNotAllowed(['POST'])
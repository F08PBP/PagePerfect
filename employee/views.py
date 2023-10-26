from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from book.models import Book
from employee.serializers import BookSerializer

# Create your views here.


#@login_required(login_url='login')
def main(request):
    response = {}
    return render(request, 'employee.html', response)

def catalogBook(request):
    all_book = Book.objects.all()
    print(all_book)
    return JsonResponse({"data": BookSerializer(all_book)}, status=200)

def settingCatalog(request):
    return

def bookFromWriter(request):
    return
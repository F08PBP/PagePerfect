from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.http import HttpResponse
from django.core import serializers

# Create your views here.


#@login_required(login_url='login')
def main(request):
    response = {}
    return render(request, 'employee.html', response)

def catalogBook(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def bookFromWriter(request):
    data = Book.objects.filter(isAccept = False).all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
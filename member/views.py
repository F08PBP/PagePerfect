from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from book.models import Book
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from main.models import Member


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()

    context = {
        'name': request.user.username,
        'books': books,
    }

    return render(request, "memberMember.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:landing'))
    return response

@login_required(login_url='/login')
def get_books_json(request):
    books_user = Book.objects.filter()
    return HttpResponse(serializers.serialize('json', books_user))

# @login_required(login_url='/login')
# def get_books_user(request, id):
#     books_dibeli = Book.objects.filter(user=request.user)

@login_required(login_url='/login')
def show_books_bought(request):
    member = Member.objects.get(user=request.user)

    context = {
        'name': request.user.username,
        'books': member.books_bought,
    }

    return render(request, "buku_dibeli.html", context)

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
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from member.forms import MessageForm
from member.models import Message
from random import randint

def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse('member:show_main'))
            return response
    else:
        form = MessageForm()
    context = {'form': form, 'name': request.user.username}
    return render(request, 'add_message.html', context)

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    member = get_object_or_404(Member, user=request.user)
    uang = member.money    
    messages = Message.objects.all()

    if (messages.__len__() == 0):
        random_message = "Keep on Reading - PerfectPage"

    else :
        random_index = randint(0, messages.__len__()-1)
        random_message = messages[random_index]

    context = {
        'name': request.user.username,
        'books': books,
        'money': uang,
        'message' : random_message,
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


@login_required(login_url='/login')
def show_books_bought(request):
    member = Member.objects.all().filter(user=request.user)[0]
    books = member.books_bought

    context = {
        'name': request.user.username,
        'books':books
    }

    return render(request, "buku_dibeli.html", context)

@login_required(login_url='/login')
def get_money(request):
    member = get_object_or_404(Member, user=request.user)
    uang = member.money
    return HttpResponse(uang)

@csrf_exempt
def add_money(request):
    if request.method == 'POST':
            new_money = int(request.POST.get('newMoney'))  # Get the new money amount from the request
            member = get_object_or_404(Member, user=request.user)
            member.money += new_money
            member.save()
            return JsonResponse({'success': True, 'new_money': member.money})
    

def get_pesanan(request):
    member = get_object_or_404(Member, user=request.user)
    pesanan = member.pesanan
    return HttpResponse(pesanan)

@login_required(login_url='/login')
def tambah_ke_keranjang(request, **kwargs):
    member = get_object_or_404(Member, user=request.user)
    book = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    if book in request.user.member.buku_dibeli.all():
        messages.info(request, 'Book is already in your cart')
        return redirect(reverse('member:show_main'))

def shopping_cart(request):
    books = Book.objects.all()
    member = get_object_or_404(Member, user=request.user)
    uang = member.money
    context = {
        'name': request.user.username,
        'books': books,
        'money': uang,
    }

    return render(request, "shopping_cart.html", context)

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json
from django.http import HttpResponseRedirect, HttpResponseNotFound
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
from employee.models import Catalog
from member.models import CartItem, BoughtItem, PurchasedItem
from copy import deepcopy


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    member = get_object_or_404(Member, user=request.user)
    uang = member.money
    context = {
        'name': request.user.username,
        'books': books,
        'money': uang,
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
    member = Member.objects.get(user=request.user)
    
    bought_items = BoughtItem.objects.filter(member=member)

    transactions_info = []
    for bought_item in bought_items:
        purchased_items = bought_item.purchaseditem_set.all()
        books_in_transaction = [{"title": purchased_item.book.title, "quantity": purchased_item.quantity} for purchased_item in purchased_items]
        transactions_info.append({
            "transaction_id": bought_item.id,
            "books": books_in_transaction,
            "date_added": bought_item.date_added,
            "notes": bought_item.notes
        })

    context = {
        'name': request.user.username,
        'transactions_info': transactions_info
    }

    return render(request, "buku_dibeli.html", context)

def get_cart(request):
    member = Member.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(member=member)

    return HttpResponse(serializers.serialize('json', cart_items))

@csrf_exempt
@login_required(login_url='/login')
def add_book_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        quantity = data.get('quantity')

        member = Member.objects.get(user=request.user)

        book, _ = Book.objects.get_or_create(title=title)

        cart_item, created = CartItem.objects.get_or_create(member=member, book=book)
        
        if not created:
            cart_item.quantity += quantity  # Menambahkan jumlah jika item sudah ada
        else:
            cart_item.quantity = quantity  # Atur jumlah baru jika item baru dibuat
        cart_item.save()

        cart_items = CartItem.objects.filter(member=member)
        cart_items_info = [{"title": item.book.title, "quantity": item.quantity} for item in cart_items]

        print(cart_items_info)

        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

@csrf_exempt
@login_required(login_url='/login')
def add_book_to_cart_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        quantity = data['quantity']

        member = Member.objects.get(user=request.user)

        book, _ = Book.objects.get_or_create(title=title)

        cart_item, created = CartItem.objects.get_or_create(member=member, book=book)
        
        if not created:
            cart_item.quantity += quantity  # Menambahkan jumlah jika item sudah ada
        else:
            cart_item.quantity = quantity  # Atur jumlah baru jika item baru dibuat
        cart_item.save()

        return JsonResponse({'status': 'success', 'message': 'Cart Successed'}, status=200)
    else:
        return HttpResponseNotFound({'status': 'error', 'message': 'Invalid request'}, status=404)
    
@csrf_exempt
@login_required(login_url='/login')
def edit_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        quantity = data.get('quantity')

        member = Member.objects.get(user=request.user)

        book, _ = Book.objects.get_or_create(title=title)

        cart_item, _ = CartItem.objects.get_or_create(member=member, book=book)

        cart_item.quantity = quantity

        cart_item.save()

        return JsonResponse({"success": True})
    return JsonResponse({"success": False})

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
    member = Member.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(member=member)
    uang = member.money

    total_harga = 0
    for i in cart_items:
        if i.book.harga == None:
            i.book.harga = 100000

        total_harga += i.book.harga*i.quantity

    cart_items = [{"title": item.book.title, "quantity": item.quantity, "harga": item.book.harga} for item in cart_items]

    context = {
        'name': request.user.username,
        'cart_items': cart_items,
        'uang': uang,
        'total_harga': total_harga,
    }

    return render(request, "shopping_cart.html", context)

def delete_cart(request, title):
    member = Member.objects.get(user=request.user)
    book = Book.objects.get(title=title)
    cart_item = CartItem.objects.filter(member=member, book=book).first()

    if cart_item:
        cart_item.delete()
    else:
        # Handle the case where the cart item doesn't exist
        pass

    return redirect('member:shopping_cart')

@csrf_exempt
def confirm_purchase(request):
    if request.method == 'POST':
        member = Member.objects.get(user=request.user)
        data = json.loads(request.body)
        notes = data.get('purchaseNotes', '')

        cart_items = CartItem.objects.filter(member=member)
        bought_item = BoughtItem(
            member=member,
            notes=notes,
        )
        bought_item.save()
        
        for item in cart_items:
            PurchasedItem.objects.create(
                bought_item=bought_item,
                member=member,
                book=item.book,
                quantity=item.quantity,
            )

        cart_items.delete()
        
        # Kembali ke halaman dengan menggunakan AJAX response
        return JsonResponse({'status': 'success', 'message': 'Purchase confirmed'}, status=200)
    else:
        return HttpResponseNotFound({'status': 'error', 'message': 'Invalid request'}, status=404)
    
@csrf_exempt
def confirm_purchase_flutter(request):
    if request.method == 'POST':
        member = Member.objects.get(user=request.user)
        data = json.loads(request.body)
        notes = data["notes"]

        cart_items = CartItem.objects.filter(member=member)
        bought_item = BoughtItem(
            member=member,
            notes=notes,
        )
        bought_item.save()

        total_price = 0
        for item in cart_items:
            # Update jumlah_buku and jumlah_terjual
            book = item.book
            book.jumlah_buku -= item.quantity
            book.jumlah_terjual += item.quantity
            book.save()

            # Calculate total price
            total_price += item.quantity * book.harga

            # Create PurchasedItem
            PurchasedItem.objects.create(
                bought_item=bought_item,
                member=member,
                book=item.book,
                quantity=item.quantity,
            )

        # Check if member has enough money
        if member.money >= total_price:
            # Deduct total price from member's money
            member.money -= total_price
            member.save()
            # Delete cart items after purchase
            cart_items.delete()

            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Purchase confirmed', 'money': member.money}, status=200)
        else:
            # Return error response if not enough money
            return JsonResponse({'status': 'error', 'message': 'Not enough money'}, status=400)
    else:
        return HttpResponseNotFound({'status': 'error', 'message': 'Invalid request'}, status=404)

def show_transaction(request):
    if request.user.is_authenticated:
        member = Member.objects.get(user=request.user)
        data = BoughtItem.objects.filter(member = member)
        
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        return HttpResponseNotFound({'status': 'error', 'message': 'Invalid request'}, status=404)
        

def show_purchased_item(request, id):
    member = Member.objects.get(user=request.user)
    bought_item = BoughtItem.objects.get(member=member, pk=id)
    purchased_items = PurchasedItem.objects.filter(member=member, bought_item=bought_item)

    return HttpResponse(serializers.serialize("json", purchased_items), content_type="application/json")

def get_books_for_json(request):
    catalog_entries = Catalog.objects.filter(isShowToMember = True).all()
    book_ids = catalog_entries.values_list('book')
    books = Book.objects.filter(pk__in=book_ids, statusAccept="ACCEPT")
    books_data = serializers.serialize('json', books)
    books_list = json.loads(books_data)
    return JsonResponse(books_list, safe=False)

def get_books_for_json_by_title(request, title):
    catalog_entries = Catalog.objects.filter(isShowToMember=True).all()
    book_ids = catalog_entries.values_list('book')
    books = Book.objects.filter(pk__in=book_ids, statusAccept="ACCEPT", title__icontains=title)
    books_data = serializers.serialize('json', books)
    books_list = json.loads(books_data)
    return JsonResponse(books_list, safe=False)

def show_cart_json(request):
    member = Member.objects.get(user=request.user)
    data = CartItem.objects.filter(member = member)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_money_flutter(request):
    if request.method == 'POST':
        member = Member.objects.get(user=request.user)
        data = json.loads(request.body)
        money = int(data["uang"])
        member.money += money
        member.save()
        return JsonResponse({'status': 'success', 'message': 'Add money successed', 'money': member.money}, status=200)
    else:
        return HttpResponseNotFound({'status': 'error', 'message': 'Invalid request'}, status=404)

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Member, Employee, Author
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import json

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            role = None

            if Member.objects.filter(user=user).exists():
                role = 'Member'
            elif Author.objects.filter(user=user).exists():
                role = 'Writer'
            elif Employee.objects.filter(user=user).exists():
                role = 'Employee'

            if role is not None:

                if role == 'Member':
                    return redirect('main:show_mainMember')
                elif role == 'Writer':
                    return redirect('main:show_mainWriter')
                else:
                    return redirect('main:show_mainEmployee')
            else :
                return redirect('main:landing')
            
    context = {}
    return render(request, 'formLogin.html', context)


def register(request):
    if request.method == 'POST':
        if 'role' in request.POST:
            name = request.POST.get('username')
            password = request.POST.get('password')

            hashed_password = make_password(password)

            if request.POST['role'] == 'Member':
                user = User.objects.create(username=name, password=hashed_password)
                member = Member(user=user)
                member.save()
                return JsonResponse({'success': True})
            elif request.POST['role'] == 'Writer':
                user = User.objects.create(username=name, password=hashed_password)
                writer = Author(user=user)
                writer.save()
                return JsonResponse({'success': True})
            elif request.POST['role'] == 'Employee':
                user = User.objects.create(username=name, password=hashed_password)
                employee = Employee(user=user)
                employee.save()
                return JsonResponse({'success': True})
            return JsonResponse({'success': False, 'error_message': 'Invalid registration data'})
    return render(request, 'formRegister.html')


@login_required(login_url='/login')
def show_mainMember(request):

    context = {
        'name': request.user.username,
    }

    return render(request, "mainMember.html", context)

@login_required(login_url='/login')
def show_mainWriter(request):

    context = {
        'name': request.user.username,
    }

    return render(request, "mainWriter.html", context)

@login_required(login_url='/login')
def show_mainEmployee(request):
    return redirect('employee:employee_page')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:landing'))
    return response




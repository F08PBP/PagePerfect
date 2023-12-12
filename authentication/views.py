from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import Author, Employee, Member

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # Menentukan role pengguna
            role = None
            if Member.objects.filter(user=user).exists():
                role = 'Member'
            elif Author.objects.filter(user=user).exists():
                role = 'Writer'
            elif Employee.objects.filter(user=user).exists():
                role = 'Employee'

            # Mengirimkan respons JSON ke Flutter
            if role:
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "role": role,
                    "message": "Login sukses!"
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, role pengguna tidak ditemukan."
                }, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali username atau kata sandi."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)


@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
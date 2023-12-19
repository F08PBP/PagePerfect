from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Member, Employee, Author

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        money = 0
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            # Status login sukses.

            role = get_user_role(user)
            money = get_user_money(user)
            response_data = {
                "username": user.username,
                "status": True,
                "role": role,
                "message": "Login sukses!"
            }

            if role == 'Member':
                response_data['money'] = money

            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali username atau kata sandi."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

def get_user_role(user):
    if Member.objects.filter(user=user).exists():
        return 'Member'
    elif Author.objects.filter(user=user).exists():
        return 'Writer'
    elif Employee.objects.filter(user=user).exists():
        return 'Employee'
    else:
        return 'unknown' 

def get_user_money(user):
    money = 0

    if Member.objects.filter(user=user).exists():
        money = Member.objects.get(user=user).money 

    return money

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



@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role', 'Member')  # Default role is Member

        # Buat user baru
        user = User.objects.create_user(username=username, password=password)

        # Setel role dan atribut tambahan sesuai kebutuhan
        if role == 'Member':
            member = Member.objects.create(user=user, money=100000)
        elif role == 'Writer':
            author = Author.objects.create(user=user)
        elif role == 'Employee':
            employee = Employee.objects.create(user=user)

        return JsonResponse({
            'status': True,
            'message': 'Registrasi sukses!',
        })

    return JsonResponse({
        'status': False,
        'message': 'Metode HTTP tidak didukung.',
    }, status=405)

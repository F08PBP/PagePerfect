from django.urls import path
from . import views
from main.views import register, login_user, landing, logout_user, show_main

app_name = 'main'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('mainMember/', show_main, name='show_main'),
    path('logout/', logout_user, name='logout')
]

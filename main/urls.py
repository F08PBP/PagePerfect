from django.urls import path
from . import views
from main.views import register, login_user, landing, logout_user, show_mainMember, show_mainWriter, show_mainEmployee
app_name = 'main'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('mainMember/', show_mainMember, name='show_mainMember'),
    path('mainWriter/', show_mainWriter, name='show_mainWriter'),
    path('mainEmployee/', show_mainEmployee, name='show_mainEmployee'),
    path('logout/', logout_user, name='logout')
]

from os import name
from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login'),
    path('home',views.home,name='home'),
    path('profile',views.Profile,name='profile'),
    path('logout' ,views.Logout,name='logout'),
    path('register',views.register,name='register'),
    path('post',views.create_post,name='post'),
    path ('update',views.update_profile,name='update')
]
from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('login/',views.loginuser,name='loginuser'),
    path('registartion/', views.registration, name='registration'),
    path('after_registration',views.after_registration,name='after_registration'),
    path('dashboard', views.userdashboard, name='userdashboard'),

]
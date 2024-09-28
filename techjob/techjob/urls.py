from app import views
from django.urls import path

urlpatterns = [
    path('a', views.login, name='login'),
    path('cadastro/',views.cadastro, name = 'cadastro'),
    path('',views.home,name = 'home'),
]

from app import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/',views.cadastro, name = 'cadastro'),
]

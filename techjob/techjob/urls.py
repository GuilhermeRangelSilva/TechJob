from app import views
from django.urls import path

urlpatterns = [
    path('',views.cadastro, name = 'cadastro'),
]

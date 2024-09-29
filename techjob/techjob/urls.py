from app import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('cadastro/',views.cadastro, name = 'cadastro'),
    path('home/',views.home,name = 'home'),
    path('usuario_freelancer/',views.freelancer, name = 'freelancer'),
    path('usuario_empresa/',views.empresa, name = 'empresa'),
    path('projeto/',views.projeto, name = 'projeto')
]

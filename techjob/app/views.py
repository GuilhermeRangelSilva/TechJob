from django.shortcuts import render

def cadastro(request):
    return render(request, 'usuario/cadastro.html')
def login(request):
    return render(request, 'usuario/login.html')
def home(request):
    return render(request, 'usuario/home.html')
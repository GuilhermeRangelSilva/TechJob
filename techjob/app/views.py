from django.shortcuts import render

def cadastro(request):
    return render(request, 'usuario/cadastro.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Freelancer, Empresa
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'usuario/home.html')

def freelancer(request):
    return render(request, 'usuario/freelancer.html')

def empresa(request):
    return render(request, 'usuario/empresa.html')

def projeto(request):
    return render(request, 'usuario/projeto.html')

def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        tipo_usuario = request.POST.get('tipo_usuario')

        if password != confirm_password:
            messages.error(request, "As senhas não correspondem.")
            return render(request, 'usuario/cadastro.html', {
                'usuario': usuario,
                'tipo_usuario': tipo_usuario,
                'nome': request.POST.get('nome'),
                'cpf': request.POST.get('cpf'),
                'email_freelancer': request.POST.get('email_freelancer'),
                'github': request.POST.get('github'),
                'nome_empresa': request.POST.get('nome_empresa'),
                'cnpj': request.POST.get('cnpj'),
                'email_empresa': request.POST.get('email_empresa'),
            })

        if Usuario.objects.filter(username=usuario).exists():
            messages.error(request, "O nome de usuário já está em uso.")
            return render(request, 'usuario/cadastro.html', {
                'usuario': usuario,
                'tipo_usuario': tipo_usuario,
                'nome': request.POST.get('nome'),
                'cpf': request.POST.get('cpf'),
                'email_freelancer': request.POST.get('email_freelancer'),
                'github': request.POST.get('github'),
                'nome_empresa': request.POST.get('nome_empresa'),
                'cnpj': request.POST.get('cnpj'),
                'email_empresa': request.POST.get('email_empresa'),
            })

        user = Usuario(username=usuario, password=make_password(password), tipo_usuario=tipo_usuario)
        user.save()

        if tipo_usuario == 'freelancer':
            nome = request.POST.get('nome')
            cpf = request.POST.get('cpf')
            email_freelancer = request.POST.get('email_freelancer')
            github = request.POST.get('github', '')  

            freelancer = Freelancer(user=user, nome=nome, cpf=cpf, email_freelancer=email_freelancer, github=github)
            freelancer.save()
            messages.success(request, "Freelancer cadastrado com sucesso!")
        
        elif tipo_usuario == 'empresa':
            nome_empresa = request.POST.get('nome_empresa')
            cnpj = request.POST.get('cnpj')
            email_empresa = request.POST.get('email_empresa')

            empresa = Empresa(user=user, nome_empresa=nome_empresa, cnpj=cnpj, email_empresa=email_empresa)
            empresa.save()
            messages.success(request, "Empresa cadastrada com sucesso!")

        return redirect('home')

    return render(request, 'usuario/cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "Credenciais inválidas.")
            return render(request, 'usuario/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'usuario/login.html')

def perfil(request):
    if request.user.is_authenticated:
        if request.user.tipo_usuario == 'freelancer':
            return redirect('freelancer')  
        elif request.user.tipo_usuario == 'empresa':
            return redirect('empresa')  
    else:
        return redirect('login')  

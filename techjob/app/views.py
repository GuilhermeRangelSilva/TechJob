from django.shortcuts import render, redirect
from .forms import UsuarioForms, FreelancerForms, EmpresaForms
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
        usuario_form = UsuarioForms(request.POST)
        if usuario_form.is_valid():
            usuario = usuario_form.save()

           
            if usuario.tipo_usuario == 'freelancer':
                freelancer_form = FreelancerForms(request.POST)
                if freelancer_form.is_valid():
                    freelancer = freelancer_form.save(commit=False)
                    freelancer.usuario = usuario
                    freelancer.save()
                    return redirect('home')  

            elif usuario.tipo_usuario == 'empresa':
                empresa_form = EmpresaForms(request.POST)
                if empresa_form.is_valid():
                    empresa = empresa_form.save(commit=False)
                    empresa.usuario = usuario
                    empresa.save()
                    return redirect('home') 

    else:
        usuario_form = UsuarioForms()
        freelancer_form = FreelancerForms()
        empresa_form = EmpresaForms()

    return render(request, 'usuario/cadastro.html', {
        'usuario_form': usuario_form,
        'freelancer_form': freelancer_form,
        'empresa_form': empresa_form,
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('usuario/home.html') 
        else:
            return render(request, 'usuario/login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'usuario/login.html')

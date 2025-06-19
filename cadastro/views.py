from django.shortcuts import render
from .models import CadastrarUsuario

def home(request):
    return render(request, 'home.html', name="home")

def cadastroUsuarioPage(request):
    return render(request, 'cadastro.html', name="cadastro")

def CadastrarUsuario(request):
    NovoUsuario = CadastrarUsuario()
    
    NovoUsuario.nome = request.POST.get('nome')
    NovoUsuario.sobrenome = request.POST.get('sobrenome')
    NovoUsuario.sexo = request.POST.get('sexo')
    NovoUsuario.dia_nasc = request.POST.get('dia_nasc')
    NovoUsuario.mes_nasc = request.POST.get('mes_nasc')
    NovoUsuario.ano_nasc = request.POST.get('ano_nasc')
    NovoUsuario.cpf = request.POST.get('cpf')
    NovoUsuario.telefone = request.POST.get('telefone')
    NovoUsuario.email = request.POST.get('email')
    
    NovoUsuario.save()
    
    NovoUsuario = {
        'NovoUsuario': CadastrarUsuario.objects.all()    
    }

    return render(request, 'home.html', context=NovoUsuario)

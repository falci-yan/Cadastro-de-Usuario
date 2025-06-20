from django.shortcuts import render
from .models import CadastrarUsuario

def home(request):
    usuarios = {
            'usuarios': CadastrarUsuario.objects.all()
        }

    return render(request, 'home.html', usuarios)

def cadastroUsuarioPage(request):
    return render(request, 'cadastro.html')

def criarUsuario(request):
    if request.method == 'POST':
        NovoUsuario = CadastrarUsuario()

        NovoUsuario.nome = request.POST.get('nome')
        NovoUsuario.sobrenome = request.POST.get('sobrenome')
        NovoUsuario.sexo = request.POST.get('sexo')
        NovoUsuario.cpf = request.POST.get('cpf')
        NovoUsuario.telefone = request.POST.get('telefone')
        NovoUsuario.email = request.POST.get('email')

        NovoUsuario.save()

        contexto = {
            'NovoUsuario': CadastrarUsuario.objects.all()
        }

        return render(request, 'home.html', contexto)
    
    return render(request, 'home.html')

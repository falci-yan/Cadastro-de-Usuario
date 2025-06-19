from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cadastro import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastroUsuarioPage, name='cadastro'),
    path('cadastrar_usuario/', views.CadastrarUsuario, name='cadastrar_usuario'),
] + static(settings.STATIC_URL, document_root='static/estilos.css')
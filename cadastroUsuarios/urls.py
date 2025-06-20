from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cadastro import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastroUsuarioPage, name='cadastro'),
    path('cadastro/novo/', views.criarUsuario, name='cadastrar_usuario'),
] + static(settings.STATIC_URL, document_root='static/estilos.css')
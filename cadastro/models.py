from django.db import models

class CadastrarUsuario(models.Model):
    id_cadastro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=[("masculino", "Masculino"), ("feminino", "Feminino")])
    dia_nasc = models.IntegerField()
    mes_nasc = models.CharField(max_length=20, choices=[
        ("janeiro", "Janeiro"), ("fevereiro", "Fevereiro"), ("março", "Março"),
        ("abril", "Abril"), ("maio", "Maio"), ("junho", "Junho"),
        ("julho", "Julho"), ("agosto", "Agosto"), ("setembro", "Setembro"),
        ("outubro", "Outubro"), ("novembro", "Novembro"), ("dezembro", "Dezembro"),
    ])
    ano_nasc = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)   
    email = models.EmailField(unique=True)

def __str__(self):
    return self.nome

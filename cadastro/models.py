from django.db import models

class CadastrarUsuario(models.Model):
    id_cadastro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, choices=[("masculino", "Masculino"), ("feminino", "Feminino")])
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)   
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.sexo} - {self.cpf} - {self.telefone} - {self.email}"

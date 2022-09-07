from django.db import models

# Create your models here.

class Films(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    autor = models.TextField(max_length=80)
    descricao = models.TextField(max_length=200)
    sinopse = models.TextField(max_length=5000,default="")
    imagem = models.TextField()

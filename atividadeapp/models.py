from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Animal(models.Model):
    nome = models.CharField(max_length=20)
    peso = models.DecimalField(max_digits=100, decimal_places = 2)
    altura = models.DecimalField(max_digits=100, decimal_places = 2)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField()
    categoria = models.ManyToManyField('Category', related_name= 'Animal')

    def __str__(self):
        return self.nome
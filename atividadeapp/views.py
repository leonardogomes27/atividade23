from django.shortcuts import render
from .models import Category, Animal
# Create your views here.

def index(request):
    return render('index.html')

def Category(request):
    return render()

def Animal(request):
    return render()
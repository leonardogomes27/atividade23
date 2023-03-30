from django.urls import path
from .views import index, Category, Animal

urlpatterns = [
    path('index.html', index, name = 'index'),
    path('', Category, name='Category'),
    path('', Animal, name='Animal'),
]

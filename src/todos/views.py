from django.shortcuts import render
from django.views.generic import ListView
from .models import Todos

# Create your views here.

class TodosListView(ListView):
    queryset = Todos.objects.all()
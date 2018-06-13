from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Todos
from .forms import TodosCreateForm

# Create your views here.

class TodosListView(ListView):
    queryset = Todos.objects.all()

class TodosCreateView(CreateView):
    form_class = TodosCreateForm
    template_name = "todos/add.html"
    success_url = "/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.user = self.request.user
        return super(TodosCreateView, self).form_valid(form)
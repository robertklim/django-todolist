from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Todos
from .forms import TodosCreateForm

# Create your views here.

class TodosListView(ListView):
    queryset = Todos.objects.all()

class TodosDetailView(DetailView):
    queryset = Todos.objects.all()

class TodosCreateView(LoginRequiredMixin, CreateView):
    form_class = TodosCreateForm
    login_url = '/login/' # Default can also be set in settings as LOGIN_URL = '/login/'
    template_name = "todos/add.html"
    # success_url = "/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.user = self.request.user
        return super(TodosCreateView, self).form_valid(form)
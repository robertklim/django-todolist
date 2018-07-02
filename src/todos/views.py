from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View
from .models import Todos
from .forms import TodosCreateForm

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render (request, "home.html", {})

        user = request.user
        is_following_user_ids = [x.user.id for x in user.is_following.all()]
        qs = Todos.objects.filter(user__id__in=is_following_user_ids).order_by("-updated")[:3]#, public=True)

        return render (request, "todos/home-feed.html", {'object_list': qs})

class TodosListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

class TodosDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

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

class TodosUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TodosCreateForm
    login_url = '/login/' # Default can also be set in settings as LOGIN_URL = '/login/'
    template_name = "todos/update.html"
    # success_url = "/"

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
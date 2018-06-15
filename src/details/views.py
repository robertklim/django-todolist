from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import DetailsCreateForm
from .models import Details

# Create your views here.

class DetailsListView(ListView):
    
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

class DetailsDetailView(DetailView):
   
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

class DetailsCreateView(LoginRequiredMixin, CreateView):
    form_class = DetailsCreateForm
    login_url = '/login/' # Default can also be set in settings as LOGIN_URL = '/login/'
    template_name = "details/add.html"

    def get_form_kwargs(self):
        kwargs = super(DetailsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.user = self.request.user
        return super(DetailsCreateView, self).form_valid(form)

class DetailsUpdateView(LoginRequiredMixin, UpdateView):
    form_class = DetailsCreateForm
    login_url = '/login/' # Default can also be set in settings as LOGIN_URL = '/login/'
    template_name = "details/update.html"

    def get_form_kwargs(self):
        kwargs = super(DetailsUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Now I can customize form
        instance.user = self.request.user
        return super(DetailsUpdateView, self).form_valid(form)
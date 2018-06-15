from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import DetailsForm
from .models import Details

# Create your views here.

class DetailsListView(ListView):
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

class DetailsDetailView(DetailView):
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

class DetailsCreateView(CreateView):
    form_class = DetailsForm
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)

class DetailsUpdateView(UpdateView):
    form_class = DetailsForm
    def get_queryset(self):
        return Details.objects.filter(user=self.request.user)
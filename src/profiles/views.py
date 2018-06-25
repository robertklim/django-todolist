from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# Create your views here.

from details.models import Details
from todos.models import Todos

User = get_user_model()

class ProfileDetailView(DetailView):
    template_name = 'profiles/profile.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['user']
        search_query = self.request.GET.get('q')
        qs = Todos.objects.filter(user=user).search(search_query)

        if qs.exists():
            context['todos'] = qs
        return context
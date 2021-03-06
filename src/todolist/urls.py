"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView, 
    PasswordResetView, 
    PasswordResetConfirmView,
    PasswordResetDoneView,
)

from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

# from django.views.generic import TemplateView

from todos.views import (
    HomeView,
#     TodosListView,
#     TodosCreateView,
#     TodosDetailView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^details/', include('details.urls', namespace='details')),
    url(r'^todos/', include('todos.urls', namespace='todos')),
    url(r'^follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^$', TodosListView.as_view(), name='home'),
    # url(r'^todos/todo/(?P<pk>\w+)/$', TodosDetailView.as_view(), name='todo'),
    # url(r'^todos/add/$', TodosCreateView.as_view(), name='add'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
     url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password_reset_done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
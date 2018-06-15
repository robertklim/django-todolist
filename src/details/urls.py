from django.conf.urls import url

from .views import (
    DetailsCreateView,
    DetailsDetailView,
    DetailsListView,
    DetailsUpdateView,
)

urlpatterns = [
    url(r'^$', DetailsListView.as_view(), name='home'),
    url(r'^add/$', DetailsCreateView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/update/$', DetailsUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$', DetailsDetailView.as_view(), name='details'),
]
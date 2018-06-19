from django.conf.urls import url

from todos.views import (
    TodosListView,
    TodosCreateView,
    TodosDetailView,
    TodosUpdateView,
)

urlpatterns = [
    url(r'^$', TodosListView.as_view(), name='home'),
    url(r'^todo/(?P<pk>\w+)/$', TodosDetailView.as_view(), name='todo'),
    url(r'^todo/(?P<pk>\d+)/update/$', TodosUpdateView.as_view(), name='update'),
    url(r'^add/$', TodosCreateView.as_view(), name='add'),
]
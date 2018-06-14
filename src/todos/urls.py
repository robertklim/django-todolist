from django.conf.urls import url

from todos.views import (
    TodosListView,
    TodosCreateView,
    TodosDetailView,
)

urlpatterns = [
    url(r'^$', TodosListView.as_view(), name='home'),
    url(r'^todo/(?P<pk>\w+)/$', TodosDetailView.as_view(), name='todo'),
    url(r'^add/$', TodosCreateView.as_view(), name='add'),
]
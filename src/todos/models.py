from django.conf import settings
from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from .validators import validate_expires

# Create your models here.

User = settings.AUTH_USER_MODEL

class TodosQuerySet(models.query.QuerySet):
    def search(self, query):    # Todos.objects.all().search(query)
        if query:
            query = query.strip()
            return self.filter(
                Q(title__icontains=query)|
                Q(entry__icontains=query)|
                Q(details__description__icontains=query)|
                Q(details__keywords__icontains=query)
                ).distinct()
        else:
            return self

class TodosManager(models.Manager):
    def get_queryset(self):
        return TodosQuerySet(self.model, using=self._db)

    def search(self, query):    # Todos.objects.search(query)
        return self.get_queryset().filter(title__icontains=query)

class Todos(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=128)
    entry       = models.CharField(max_length=512, null=True, blank=True)
    expires     = models.DateField(null=True, blank=True, validators=[validate_expires])
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    objects = TodosManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f'/todo/{self.pk}'
        return reverse('todos:todo', kwargs={'pk': self.pk})
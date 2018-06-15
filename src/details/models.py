from django.conf import settings
from django.db import models

from todos.models import Todos

# Create your models here.

class Details(models.Model):
    # associations
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    todo        = models.ForeignKey(Todos)
    # details data
    keywords    = models.TextField(help_text='Separete each bo comma')
    description = models.TextField(blank=True, null=True, help_text='Separete each bo comma')
    public      = models.BooleanField(default=True)
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    # Default ordering
    class Meta:
        ordering = ['-updated', '-timestamp']
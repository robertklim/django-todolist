from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from todos.models import Todos

# Create your models here.

class Details(models.Model):
    # associations
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    todo        = models.ForeignKey(Todos)
    # details data
    keywords    = models.TextField(help_text='Separete each by comma')
    description = models.TextField(blank=True, null=True)
    public      = models.BooleanField(default=True)
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    def get_absolute_url(self):
        # return f'/todo/{self.pk}'
        return reverse('details:details', kwargs={'pk': self.pk})

    # Default ordering
    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_keywords(self):
        return self.keywords.split(', ')

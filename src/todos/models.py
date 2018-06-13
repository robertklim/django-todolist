from django.conf import settings
from django.db import models
from .validators import validate_expires

# Create your models here.

User = settings.AUTH_USER_MODEL

class Todos(models.Model):
    user        = models.ForeignKey(User)
    title       = models.CharField(max_length=128)
    entry       = models.CharField(max_length=512, null=True, blank=True)
    expires     = models.DateField(null=True, blank=True, validators=[validate_expires])
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.

class Todos(models.Model):
    title       = models.CharField(max_length=128)
    entry       = models.CharField(max_length=512, null=True, blank=True)
    expires     = models.DateField(null=True, blank=True)
    timestamp   = models.DateField(auto_now_add=True)
    updated     = models.DateField(auto_now=True)


    def __str__(self):
        return self.title
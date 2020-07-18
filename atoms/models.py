from django.db import models


# Create your models here.
class Atoms(models.Model):
    name = models.CharField('Name', max_length=32)
    description = models.CharField('Description', max_length=256)
from django.db import models

from atom_mgmt.models import Atom


class Track(models.Model):
    atom_id = models.ForeignKey(Atom, on_delete=models.PROTECT)
    score = models.IntegerField()
    track_date = models.DateField()
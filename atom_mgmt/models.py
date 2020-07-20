from django.db import models

from user_mgmt.models import Users


class Atom(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    atom_status = models.CharField(max_length=12)
    atom_name = models.CharField(max_length=16)
    atom_weight = models.IntegerField(default=2)
    atom_desc = models.CharField(max_length=256)
    atom_category = models.CharField(max_length=24)
    atom_position = models.IntegerField(null=True)
    track_frequency = models.CharField(max_length=24)
    cheat_days = models.IntegerField(default=0)
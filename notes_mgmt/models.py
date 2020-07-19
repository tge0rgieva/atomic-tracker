from django.db import models

from user_mgmt.models import Users


class Notes(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    note_date = models.DateField()
    user_note = models.CharField(max_length=128)

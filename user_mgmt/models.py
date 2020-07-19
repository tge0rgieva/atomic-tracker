from django.db import models


class Users(models.Model):
    user_status = models.CharField(max_length=12)
    user_name = models.CharField(max_length=24)
    user_password = models.CharField(max_length=128)
    user_mail = models.CharField(max_length=320)
    user_mail_conf = models.BooleanField()
    user_date_created = models.DateField()


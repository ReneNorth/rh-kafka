from django.db import models

from django.db import models


class Contractor(models.Model):
    name = models.CharField(max_length=255)
    is_driver = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    document_verified_driver = models.BooleanField(default=False)
    document_verified_courier = models.BooleanField(default=False)

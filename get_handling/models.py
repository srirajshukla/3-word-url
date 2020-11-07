from django.db import models

import api.shortener


# Create your models here.

class long_and_short(models.Model):
    long_url = models.CharField(max_length=500)
    shortform = models.CharField(max_length=30, null=True, editable=False, default=api.shortener.short(long_url))

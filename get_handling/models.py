from django.db import models
from django.utils.translation import gettext_lazy as _

import api.shortener


# Create your models here.

class long_and_short(models.Model):
    long_url = models.CharField(max_length=500)
    shortform = models.CharField(max_length=30, null=True, default=api.shortener.short(long_url))

    class DurationHours(models.TextChoices):
        ONE_HOUR = "1", _("One Hr")
        THREE_HOUR = "3", _("Three Hrs")
        SIX_HOUR = "6", _("Six Hrs")
        TWENTRYFOUR_HOUR = "24", _("Twentyfour Hrs")
        FOREVER = "0", _("Forever")

    duration = models.CharField(
        max_length=2,
        choices=DurationHours.choices,
        default=DurationHours.FOREVER
    )

    created = models.DateTimeField(auto_now_add=True)
    # Uncomment for testing purposes only
    # Causes key error while migration because auto_now_add is uneditable by default
    # created.editable = True


    def __str__(self):
        return self.long_url

    def __repr__(self):
        return f'Long: {self.long_url}\nShort: {self.shortform}\nCreated on: {self.created}\nDuration: {self.duration}'

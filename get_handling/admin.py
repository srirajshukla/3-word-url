from django.contrib import admin

from .models import long_and_short


# Register your models here.

@admin.register(long_and_short)
class long_and_short_admin(admin.ModelAdmin):
    list_display = ("long_url", "shortform", "created", "duration")
    list_filter = ("created", "duration")
    search_fields = ("long_url", "shortform")

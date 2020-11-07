from django.contrib import admin

from .models import long_and_short


# Register your models here.


class lasadmin(admin.ModelAdmin):
    fields = ['long_url']


admin.site.register(long_and_short, lasadmin)

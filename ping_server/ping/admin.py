from django.contrib import admin

from .models import Domains


@admin.register(Domains)
class DomainsAdmin(admin.ModelAdmin):
    pass


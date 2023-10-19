from django.contrib import admin

from .models import Schema


@admin.register(Schema)
class SchemeAdmin(admin.ModelAdmin):
    list_display =('name', 'deadline',)
    list_filter = ('deadline',)
    search_fields = ('name',)

from django.contrib import admin

from .models import Rep


@admin.register(Rep)
class RepAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("name",)}

from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("nome", "slug", "autor", "criado", "atualizado")
    prepopulated_fields = {"slug": ("nome",)}

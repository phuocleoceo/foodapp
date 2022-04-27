from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    # Sử dụng name làm khuôn cho slug
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)


# Register your models here.
admin.site.register(Category, CategoryAdmin)

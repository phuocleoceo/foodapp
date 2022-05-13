from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    # Sử dụng name làm khuôn cho slug
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "price",  "is_available", "modified_date", "category")


# Register your models here.
admin.site.register(Product, ProductAdmin)

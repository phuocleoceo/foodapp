from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


class AdminUser(UserAdmin):
    # Các trường cho phép hiển thị
    list_display = ("username", "email", "first_name", "last_name", "date_joined", "last_login", "is_active")
    # Trường cho phép click để truy cập vào thông tin user
    list_display_links = ("email", "first_name", "last_name")
    # Trường chỉ cho phép đọc
    readonly_fields = ("date_joined", "last_login")
    # Sắp xếp theo
    ordering = ("date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(User, AdminUser)

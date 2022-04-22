from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None):
        """
        Hàm tạo mới 1 user 
        """
        # Validate
        if not username:
            raise ValueError("Username is required !")
        if not email:
            raise ValueError("Email is required !")

        # Tạo user entity
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):
        """
        Hàm tạo super user, dùng lại hàm Create_User
        """
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_permission(self, permission, obj=None):
        return self.is_admin

    def has_module_permission(self, add_label):
        return True

import os
from django import setup
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodapp.settings")
setup()

User.objects.create_superuser('phuocleoceo', 'ht10082001@gmail.com', 'phuocleoceo')

from .models import User
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone_number", "password"]

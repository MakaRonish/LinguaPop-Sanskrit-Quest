from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "User Name",
            "email": "Email",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter a Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your Email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["placeholder"] = "Enter Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"

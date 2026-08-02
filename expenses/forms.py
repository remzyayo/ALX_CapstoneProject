from django import forms
from .models import Task, Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "project", "deadline", "priority", "status",]
        widgets = {"deadline": forms.DateInput(attrs={"type": "date"}),} 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    country = CountryField().formfield(widget=CountrySelectWidget())
    phone_number = PhoneNumberField(required=True, help_text="Enter your phone number with country code.")
    class Meta:
        model = User
        fields = [
            "username",
            "country",
            "phone_number",
            "password1",
            "password2",
        ]

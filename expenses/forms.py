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
    email = forms.EmailField(required=True),
    help_text="Enter a valid email address."

    country = CountryField().formfield(
        widget=CountrySelectWidget(attrs={"id": "country"})
    )

    phone_number = PhoneNumberField(
        required=True,
        widget=forms.TextInput(attrs={"id": "phone_number"}),
        help_text="Enter your phone number with country code."
    )

    
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(),
    help_text="Choose a strong password that is at least 8 characters long, is not similar to your personal information, is not a commonly used password, and is not made up entirely of numbers."
)

    password2 = forms.CharField(
    label="Password Confirmation",
    widget=forms.PasswordInput(),
    help_text="Enter the same password again for verification."
)

    class Meta:
        model = User
        fields = [
            "username",
            "country",
            "phone_number",
            "email",
            "password1",
            "password2",
           
        ]
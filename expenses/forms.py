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

    country = CountryField().formfield(
        widget=CountrySelectWidget()
    )

    phone_number = PhoneNumberField(
        required=True,
        help_text="Enter your phone number with country code."
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="""
<ul>
<li>Your password can't be too similar to your personal information.</li>
<li>Your password must contain at least 8 characters.</li>
<li>Your password can't be a commonly used password.</li>
<li>Your password can't be entirely numeric.</li>
</ul>
"""
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
from django import forms
from .models import Task, Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

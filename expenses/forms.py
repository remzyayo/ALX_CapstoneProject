from django import forms
from .models import Task, Project

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "project", "deadline", "priority", "status",]
        widgets = {"deadline": forms.DateInput(attrs={"type": "date"}),} 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]

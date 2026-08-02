from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, filters, generics
from .models import Expense, Task
from .serializer import ExpenseSerializer, RegisterSerializer
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.utils import timezone
from .forms import TaskForm, ProjectForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

from .models import Profile


User = get_user_model()

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'date']
    search_fields = ['description']
    ordering_fields = ['amount', 'date']

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        user = request.user
        expenses = Expense.objects.filter(user=user)
        total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        total_budget = expenses.aggregate(Sum('budget'))['budget__sum'] or 0
        remaining = total_budget - total_spent

        return Response({
            'total_spent': total_spent,
            'total_budget': total_budget,
            'remaining_balance': remaining
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

@login_required
def task_list(request):
        today = timezone.now().date()
        priority_filter = request.GET.get("priority")
        status_filter = request.GET.get("status")
        search_query = request.GET.get("q")
        tasks = Task.objects.filter(owner=request.user).select_related("project").order_by("deadline")

        if priority_filter:
            tasks = tasks.filter(priority=priority_filter)

        if status_filter:
             tasks = tasks.filter(status=status_filter)

        if search_query:
             tasks = tasks.filter(title__icontains=search_query)

        overdue_tasks = Task.objects.filter(owner=request.user, deadline__lt=today).exclude(status="Done")
        context = {"tasks": tasks, "overdue_tasks": overdue_tasks, "today": today, "priority_filter": priority_filter, "status_filter": status_filter, "search_query": search_query,}

        return render(request, "expenses/task_list.html", context)

@login_required
def add_task(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
           task = form.save(commit=False)
           task.owner = request.user
           task.save()
        return redirect("task_list")

    else:

        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "expenses/task_form.html", context)

@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = ProjectForm()

    return render(
        request,
        "expenses/project_form.html",
        {"form": form},
    )


def home(request):
    return redirect("task_list")


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.country = form.cleaned_data["country"]
            profile.phone_number = form.cleaned_data["phone_number"]
            profile.save()
            login(request, user)
            return redirect("task_list")

    else:

        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )

#login view
def user_login(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect("task_list")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "registration/login.html",
        {"form": form},
    )

#Logout view
def user_logout(request):

    logout(request)

    return redirect("login")   

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, task_list
from . import views

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path("api/", include(router.urls)),
    path("task/", views.task_list, name="task_list",),
    path("add/", views.add_task, name="add_task",),
    path("", views.home, name="home"),
]
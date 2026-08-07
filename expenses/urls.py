from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, task_list, TaskViewSet
from . import views

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router = DefaultRouter()
router.register(r"tasks-api", TaskViewSet, basename="tasks-api")

urlpatterns = [
    path("api/", include(router.urls)),
    path("task/", views.task_list, name="task_list",),
    path("add/", views.add_task, name="add_task",),
    path("project/add/", views.add_project, name="add_project"),
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]

urlpatterns += router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet
from . import views

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
    path("", views.recipe_list, name="recipe_list"),
]
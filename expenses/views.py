from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Expense
from .serializer import ExpenseSerializer
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class ExpenseViewSet(viewsets.ModelViewSet):
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


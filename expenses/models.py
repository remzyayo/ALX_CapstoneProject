from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Bills', 'Bills'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    difference = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.difference = self.budget - self.amount
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.category} - ₦{self.amount}"
    




from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'category', 'amount', 'budget', 'difference', 'description', 'date']
        read_only_fields = ['id', 'user', 'difference', 'date']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        validated_data['difference'] = validated_data.get('budget', 0) - validated_data['amount']
        return super().create(validated_data)
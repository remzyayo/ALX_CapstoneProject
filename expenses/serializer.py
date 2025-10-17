from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User

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
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user   
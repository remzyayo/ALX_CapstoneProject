from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

# Register a new user
class RegisterView(generics.CreateAPIView):
    queryset = get_user_model
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all


# Login existing user
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })



User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


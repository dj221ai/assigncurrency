from django.shortcuts import render
from .models import UserBalance
from .serializers import UserBalanceSerializer, UserCreationSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from rest_framework import generics


class CreateUserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserCreationSerializer
    permission_classes = (permissions.AllowAny, )


class UserBalanceView(viewsets.ModelViewSet):
    queryset = UserBalance.objects.all()
    serializer_class = UserBalanceSerializer

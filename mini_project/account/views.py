from django.shortcuts import render
from rest_framework import viewsets
from account.serializers import UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics
import requests
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth import get_user_model
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    def create(self, request):
        pass

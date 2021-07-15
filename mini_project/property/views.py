from rest_framework import viewsets
from account.serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from property.serializers import PropertySerializers
from property.models import Property
from django.http import HttpResponse
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers


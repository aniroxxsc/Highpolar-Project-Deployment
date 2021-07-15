from rest_framework import viewsets
from account.serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from property.serializers import PropertySerializers, Faq_PropertySerializers
from property.models import Property, Favourite_Property, Faq_Property
from django.http import HttpResponse
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers
        
class Favourite_PropertyViewSet(viewsets.ModelViewSet):
    queryset = Favourite_Property.objects.all()
    serializer_class = Favourite_Property
    permission_classes = [IsAuthenticated]
    
class Faq_PropertyViewSet(viewsets.ModelViewSet):
    queryset = Faq_Property.objects.all()
    serializer_class = Faq_PropertySerializers




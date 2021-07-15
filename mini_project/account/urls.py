from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from account import views
from django.conf.urls import  url
#from account.views import ActivateUser
from django.core.mail import send_mail

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'account', views.UserViewSet)
urlpatterns = router.urls

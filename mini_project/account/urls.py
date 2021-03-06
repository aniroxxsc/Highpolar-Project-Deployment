from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from account import views
from django.conf.urls import  url
from django.core.mail import send_mail

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'account', views.UserViewSet)
urlpatterns = router.urls
# The API URLs are now determined automatically by the router.
urlpatterns += [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

urlpatterns += [re_path( r'^.*', TemplateView.as_view(template_name='index.html'))]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from property import views
from django.conf.urls import url

router = DefaultRouter()
router.register(r'property', views.PropertyViewSet,  basename='property')
router.register(r'faq', views.Faq_PropertyViewSet,  basename='faq')
urlpatterns = router.urls

urlpatterns +=[
#    path('^faq/', include('faq.urls')),
]
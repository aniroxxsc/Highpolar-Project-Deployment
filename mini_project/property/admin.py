from django.contrib import admin
from .models import Property, Favourite_Property, Faq_Property

#admin.site.register(Faq_Property)
admin.site.register(Property) 
admin.site.register(Favourite_Property)
admin.site.register(Faq_Property)

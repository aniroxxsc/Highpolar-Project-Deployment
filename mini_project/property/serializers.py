from rest_framework import serializers
from property.models import Property, Favourite_Property, Faq_Property

class Faq_PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faq_Property
        fields = '__all__'

class PropertySerializers(serializers.HyperlinkedModelSerializer):
#    faq = Faq_PropertySerializers(source='faq.question')
    class Meta:
        model = Property
        fields = '__all__'
        depth = 2

class Favourite_PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = Favourite_Property
        fields = '__all__'
from rest_framework import viewsets
from account.serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from property.serializers import PropertySerializers, Faq_PropertySerializers
from property.models import Property, Favourite_Property, Faq_Property
from django.http import HttpResponse
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

import joblib
import numpy as np
import pickle


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializers
    #authentication_classes = [authentication.TokenAuthentication]

    '''def get_authenticators(self):
        if self.action == 'create' or 'retrieve' or 'update' or 'partial_update' or 'delete':
            authentication_classes = [authentication.TokenAuthentication]'''

    def get_permissions(self):
        if self.action == 'create' or 'retrieve' or 'update' or 'partial_update' or 'delete' :
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]

    def create(self, request):  
        def bool_to_int(bool):
            if bool == "true":
                return 1
            else:
                return 0
        under_construction = bool_to_int(request.POST.get("under_construction"))
        rera = bool_to_int(request.POST.get("rera"))
        bhk_no = bool_to_int(request.POST.get("bhk_no"))
        bhk_or_rk = bool_to_int(request.POST.get("bhk_or_rk"))
        square_ft = float(request.POST.get("square_ft"))
        ready_to_move = bool_to_int(request.POST.get("ready_to_move"))
        resale = bool_to_int(request.POST.get("resale"))
        latitude = float(request.POST.get("latitude"))
        longitude = float(request.POST.get("longitude"))
        list = [under_construction, rera, bhk_no, bhk_or_rk, square_ft, ready_to_move, resale, latitude, longitude]
        arr = np.array(list)
        arr = arr.reshape(1,-1)
        model = pickle.load(open('./model/DecisionTreeRegressor.sav','rb'))
        y_pred = model.predict(arr)
        print("############here is the value#######  : " ,request.POST["cost_estimated"], "  : ###### Value #######")
#        if cost_estimated := request.POST.get("cost_estimated"):
        request.data._mutable = True
        request.POST["cost_estimated"] = y_pred
        return super().create(request)
        
class Favourite_PropertyViewSet(viewsets.ModelViewSet):
    queryset = Favourite_Property.objects.all()
    serializer_class = Favourite_Property
    permission_classes = [IsAuthenticated]
    
class Faq_PropertyViewSet(viewsets.ModelViewSet):
    queryset = Faq_Property.objects.all()
    serializer_class = Faq_PropertySerializers

#    def create(self, request):



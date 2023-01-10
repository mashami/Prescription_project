from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework import generics, mixins, status
from .serializer import DoctorSerializer, PharmacistSerializer,getPatientSerializer
from rest_framework import permissions
from .models import DoctorM
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from authentication.models import User
from rest_framework.exceptions import AuthenticationFailed 
import requests
# from django.utils.decorators import method_decorator
# from django.views.decorators.cors import cors_decorator

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class DoctorAPIView(generics.GenericAPIView,mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin):
    serializer_class= DoctorSerializer
    # permission_classes= permissions.IsAuthenticated
    # permission_classes= permissions.DjangoObjectPermissions
    
    queryset=DoctorM.objects.all()
    lookup_field='id'
    
    def post(self, request):
        return self.create(request, status.HTTP_200_OK)

    def get (self,request, id=None):
          
        return self.list(request, status.HTTP_200_OK)



class DoctorUpdate(generics.GenericAPIView):
    serializer_class=DoctorSerializer
    serializer_classes=DoctorSerializer
    lookup_field='id'
    # permission_classes=[IsAdminUser]
    def get(self,request,id):
        id=get_object_or_404(DoctorM,pk=id)
        serializer=self.serializer_classes(instance=id)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self,request,id):
        id=get_object_or_404(DoctorM,pk=id)
        data=request.data
        serializer=self.serializer_classes(data=data,instance=id)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# @method_decorator(cors_decorator(origin="*"), name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class PharmacistAPIView(generics.GenericAPIView):
    

    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    serializer_class=PharmacistSerializer
    serializer_classes=PharmacistSerializer
    lookup_field='id'
#     # permission_classes= permissions.IsAuthenticated
#     # permission_classes= permissions.DjangoObjectPermissions
    
    queryset=DoctorM.objects.all()
    lookup_field='id'
    
    # def get(self, request, id):
    #     objects = DoctorM.objects.values('DoctorName', 'medicine')
    #     serializer = PharmacistSerializer(objects, many=True)
    #     return Response(serializer.data ) 

    def get(self,request,id):
        id=get_object_or_404(DoctorM,pk=id)
        serializer=self.serializer_classes(instance=id)
        return Response(serializer.data,status=status.HTTP_200_OK)
     
    def put(self,request,id):
        id=get_object_or_404(DoctorM,pk=id)
        data=request.data
        serializer=self.serializer_classes(data=data,instance=id)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class getPatientAPI(generics.GenericAPIView):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    serializer_class=getPatientSerializer
    serializer_classes=getPatientSerializer
   
    

    # def get_user_info(email):
    #     # Send a POST request to the user verification API
    #     verify_response = requests.post('http://127.0.0.1:8000/pres/patient/', json={'email':email })

    #     if verify_response.json()['exists']:
    #         # If the user exists, send a GET request to the user info API
    #         user_id = verify_response.json()['id']
    #         info_response = requests.get(f'http://127.0.0.1:8000/pres/doctor//{user_id}')
    #         return info_response.json()
    #     else:
    #         return None

    
    def post (self,request):  
        email=request.data['email']
        
        if User.objects.filter(email=email).exists():
            return Response( status=status.HTTP_200_OK)
        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
            

@method_decorator(csrf_exempt, name='dispatch')
class PatientAPIView(generics.GenericAPIView):
    

    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    serializer_class=PharmacistSerializer
    serializer_classes=PharmacistSerializer
    lookup_field='id'
#     # permission_classes= permissions.IsAuthenticated
#     # permission_classes= permissions.DjangoObjectPermissions
    
    queryset=DoctorM.objects.all()
    lookup_field='id'
    
    

    def get(self,request,id):
        id=get_object_or_404(DoctorM,pk=id)
        serializer=self.serializer_classes(instance=id)
        return Response(serializer.data,status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework import generics, mixins,status
from .serializer import *
from .models import User
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed 
import jwt,datetime
from rest_framework.decorators import APIView
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode 
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class SignupAPI(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=UserSiliarizer
    queryset=User.objects.all()
    def post(self,request):
        return self.create(request)
    # def get(self,request):
    #     return self.list(request)

# class UserView(generics.GenericAPIView, mixins.CreateModelMixin):
#     serializer_class=UserSiliarizer
#     queryset=User.objects.all()
    
#     def post(self, request):
#         data=request.data
#         serializer=self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#=======================================================================================

class Login(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class=UserSerializerLogIn
    
    def post (self,request):  
        email=request.data['email']
        password=request.data['password']
        
        user=User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('user is not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('password is incorrect')
        
        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.utcnow()  
        }
        
        token=jwt.encode(payload,'secret', algorithm='HS256')
        response=Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={
                'jwt':token
            }
        
        return response


class UserView(APIView):
    # permission_classes=[IsAuthenticated]
    def get(self,request):
        token=request.COOKIES.get('Bearer')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthentacated')
        
        
        user=User.objects.filter(id=payload['id']).first()
        serializer=UserSiliarizer(user)
        # othor=serializer.User_name
        return Response(serializer.data)

    
class LogOut(APIView):
    def post(self,request):
        response=Response(status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('jwt')
        
        response.data={
            'message':'user has been logout successful!!' 
        }
        
        return response
#==================================================================================================
                                 #ForgetPassword
@method_decorator(csrf_exempt, name='dispatch')
class forgetPassword(APIView):   
    serializer = emailserializer
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = "*"
    def post(self, request, format=None):
        serializer = emailserializer(data=request.data)
        
        if serializer.is_valid():
            send_to = serializer.data['email']
            email_sender = settings.EMAIL_HOST_USER
            email=request.data['email']
            if User.objects.filter(email=email).exists():
            
                user=User.objects.get(email=email)
                # uidb64=urlsafe_base64_encode(smart_bytes(user.id))
                token=PasswordResetTokenGenerator().make_token(user)
                
                send_mail(
                    'Code verification' 
                    'Use this code To verify',
                    token,
                    email_sender,
                    [send_to],
                    fail_silently=False,
                )
                def __init__(self):
                    self.vri=token
                return Response({'success':True,'message':'send Email successfull to: ','Email':serializer.data},status=status.HTTP_200_OK)
            return Response({'Fail':True,'message':'this Email is not registed in our system'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class verifyToken(generics.GenericAPIView, mixins.CreateModelMixin,forgetPassword):
    serializer_class=verifyTokenSerializer 
    # def __init__(self,Token):
    #    return self.Token.vri
        
    def post(self,request):
        token=self.serializer_class(data=request.data)
        ClassF=forgetPassword()
        currentToken=ClassF.self('token')
        print()
        print()
        print()
        print(currentToken)
        print()
        print()
        print()
        serializer=self.serializer_class(data=request.data)
        if token != currentToken:
            raise AuthenticationFailed('token is incorrect')
        serializer.is_valid(raise_exception=True)
        self.create(request)
        return Response({'success':True,'message':'code verified successfull'}, status=status.HTTP_200_OK)
    
    
class SetNewPasswordAPI(generics.GenericAPIView ,mixins.UpdateModelMixin):
    serializer_class=SetNewPasswordserializer
    lookup_field='id'
    def put (self,request, id=None):
        
        return self.update(request,id)
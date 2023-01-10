from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
User=get_user_model
# Create your models here
class UserCustomerManager(BaseUserManager):
    def create_user(self,password,email,**extra_fields):
        if not email:
            raise ValueError(_('Email should be provided'))
        email=self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('The superuser should be a staff'))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('The superuser should be a active'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('This is for superuser only '))
        
        return self.create_user(email,password,**extra_fields)
    
    
class User(AbstractUser):

    first_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    User_name=models.CharField(max_length=100, blank=True, null=False,unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active=models.BooleanField(default=True)
    password=models.CharField(max_length=100)
    create_on=models.DateField(auto_now_add=True)
        
    USERNAME_FIELD='User_name'
    REQUIRED_FIELDS= ['email']
    
    objects=UserCustomerManager()
    
    def __str__(self):
        return f"<User {self.User_name,self.email}"
    @property  
    def username(self):
        return self.User_name
    @property
    def first_name(self):
        return self.first_Name
   
    @property
    def last_name(self):
        return self.Last_Name

from django.urls import path
from. import views


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
...

schema_view = get_schema_view(
   openapi.Info(
      title="Prescription APIs",
      
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mashamipaccy04@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('sign',views.SignupAPI.as_view()),
   #  path('signUp',views.UserView.as_view()),
    path('login',views.Login.as_view()),
    path('userlogedin/',views.UserView.as_view()),
    path('logout/',views.LogOut.as_view()),
    path('forgetpassword/',views.forgetPassword.as_view()),
    path('verifytoken/',views.verifyToken.as_view()),
    path('resetpassowrd',views.SetNewPasswordAPI.as_view()),
    path('auth/', include('djoser.urls.jwt')),
    
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




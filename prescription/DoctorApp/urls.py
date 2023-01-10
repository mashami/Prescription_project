from django.urls import path
from. import views
from .views import*

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('doctor/',views.DoctorAPIView.as_view()),
    path('doctor/<int:id>',views.DoctorUpdate.as_view()),
    path('pharmacist/<int:id>',views.PharmacistAPIView.as_view()),
    path('patient/', views.getPatientAPI.as_view()),
    path('getpatient/<int:id>',views.PatientAPIView.as_view()),
   #  path('update/<int:id>',views.PharmacistPUTAPI.as_view()),
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




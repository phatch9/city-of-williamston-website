from django.urls import path
from . import views
from .views import MyTokenObtainPairView, RegistrationAPIView, ContactAPIView

from rest_framework_simplejwt.views import (
    TokenRefreshView, 
)

urlpatterns = [
    path('', views.getRoutes), #calls the views getRoutes method
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('contact/', ContactAPIView.as_view(), name= 'contact') 
]

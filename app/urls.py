from django.urls import path
from .views import ResgisterView, LoginView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/register/', ResgisterView.as_view(), name='register'),
    ]
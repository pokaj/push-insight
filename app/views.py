from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken 
from .models import User
from django.http import HttpResponse

class ResgisterView(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        # token = RefreshToken.for_user(user).access_token
        return Response({'status': True, 'user': user_data, 'request_status':status.HTTP_201_CREATED})




class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data) 
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        user = User.objects.filter(email=user_data['email'])
        serialized = UserSerializer(user, many=True)
        data = {
            'details': serializer.data,
            'user_info':{
                'firstname':serialized.data[0]['firstname'],
                'lastname':serialized.data[0]['lastname'],
                'role':serialized.data[0]['role'],
                'organization':serialized.data[0]['organization'],
            }
        }

        return Response({'status': True, 'data': data, 'request_status':status.HTTP_200_OK})
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    UserCreateSerializer, UserSerializer, ProfileSerializer,UpdatePasswordSerializer
    )

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class TokenAcsessView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class= ProfileSerializer
    def get_object(self):
        return self.request.user
    
class UpdatePasswordView(UpdateAPIView):
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)

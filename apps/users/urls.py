from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import RegisterView, TokenAcsessView, ProfileUpdateView, UpdatePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenAcsessView.as_view(), name='token_access'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile_update/', ProfileUpdateView.as_view(), name='profile'),
    path('password_update/',UpdatePasswordView.as_view())
]
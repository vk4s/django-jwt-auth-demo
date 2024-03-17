from django.contrib import admin
from django.urls import path, include

from authapi.views import (
    UserCreateAPIView, LoginAPIView,
    verify_token, check_login_status, logout
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

# from views import register_user, login_user

urlpatterns = [
    path('v1/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('v1/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('v1/logout/', logout, name='user-logout'),
    path('v1/verify-token/', verify_token, name='user-verify-token'),
    path('v1/check-login-status/', check_login_status, name='user-check-login-status'),
]

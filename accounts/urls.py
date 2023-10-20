from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from accounts.Admin.views import ListUsersAPIView
from accounts.views import UserInfoAPIView, UpdateUserInfo, UserRegisterAPIView, CustomTokenObtainPairView

ADMIN_ENDPOINTS = [
    path('u/admin/list', ListUsersAPIView.as_view(), name='list-users')
]

urlpatterns = [
    path('u/create', UserRegisterAPIView.as_view(), name='create_user'),
    path('u/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('u/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('u/info', UserInfoAPIView.as_view(), name='get_user_info'),
    path('u/info/update', UpdateUserInfo.as_view(), name='user_update_user_info'),
] + ADMIN_ENDPOINTS

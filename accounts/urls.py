from django.urls import path

from accounts.views import UserInfoAPIView, UpdateUserInfo

urlpatterns = [
    path('u/info/', UserInfoAPIView.as_view(), name='get_user_info'),
    path('u/info/update/', UpdateUserInfo.as_view(), name='user_update_user_info'),
]

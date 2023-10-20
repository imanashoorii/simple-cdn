from django.urls import path

from file_manager.Admin.views import GetUserUploadedFilesAPIView
from file_manager.views import ListCreateFileAPIView

ADMIN_ENDPOINTS = [
    path('manager/admin/<int:user_id>/list', GetUserUploadedFilesAPIView.as_view(), name='list-user-files')
]

urlpatterns = [
    path('manager/upload', ListCreateFileAPIView.as_view(), name='list-create-file')
] + ADMIN_ENDPOINTS

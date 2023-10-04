from django.urls import path

from file_manager.views import ListCreateFileAPIView

urlpatterns = [
    path('manager/upload', ListCreateFileAPIView.as_view(), name='list-create-file')
]

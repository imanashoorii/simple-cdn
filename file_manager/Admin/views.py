from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from file_manager.models import FileManager
from file_manager.serializers import FileManagerSerializer


class GetUserUploadedFilesAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = FileManagerSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return FileManager.objects.select_related('user').filter(user_id=user_id).order_by('-uploaded_at')

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from file_manager.models import FileManager
from file_manager.serializers import FileManagerSerializer


class ListCreateFileAPIView(generics.ListCreateAPIView):
    queryset = FileManager.objects.all()
    serializer_class = FileManagerSerializer
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )




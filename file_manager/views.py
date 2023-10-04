# import os
#
# from rest_framework.parsers import MultiPartParser
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from file_manager.minifier.enums import MinifierEnum, MimeType
# from file_manager.minifier.factory import MinifierProviderFactory
# from file_manager.serializers import FileUploadSerializer
# from file_manager.utils import get_file_type
#
#
# class FileUploadView(APIView):
#     parser_classes = [MultiPartParser]
#     permission_classes = (IsAuthenticated, )
#
#     def post(self, request):
#
#         serializer = FileUploadSerializer(data=request.data)
#
#         if serializer.is_valid():
#             uploaded_file = serializer.validated_data.get('file')
#             minify = serializer.validated_data.get('minify', False)
#             username = request.user.username
#             target_directory = f'/opt/{username}'
#
#             name, extension = os.path.splitext(uploaded_file.name)
#
#             target_file_path = os.path.join(target_directory, f'minified_{name}.js')
#
#             if minify:
#                 file_type = get_file_type(uploaded_file)
#                 minifier_class = MinifierProviderFactory().get(file_manager=MinifierEnum.CSS_HTML_JS)
#                 uploaded_file_content = uploaded_file.read().decode('utf-8')
#                 status, result = minifier_class.minify(file_type=file_type,
#                                                        input_file=uploaded_file_content,
#                                                        output_file=target_file_path
#                                                        )
#                 return Response(
#                     {
#                         'status': status,
#                         'result': result
#                     },
#                     200
#                 )
#             return Response({'message': 'File uploaded and processed successfully.'})
#         else:
#             return Response(serializer.errors, status=400)
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




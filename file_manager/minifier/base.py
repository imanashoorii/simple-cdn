import mimetypes
from abc import ABC, abstractmethod
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile


class BaseMinifierProviderClass(ABC):

    @staticmethod
    def createInMemoryUploadFile(file_name, file_content):
        modified_content = file_content
        modified_file = BytesIO(bytes(modified_content.encode()))
        modified_file.name = file_name
        modified_file.content_type = mimetypes.guess_type(file_name)
        modified_file.size = len(modified_content)

        new_uploaded_file = InMemoryUploadedFile(
            file=modified_file,
            field_name=None,
            name=file_name,
            content_type=modified_file.content_type,
            size=modified_file.size,
            charset=None,
        )

        return new_uploaded_file

    @abstractmethod
    def minify_html(self, file_name: str = None, file_content: str = None):
        raise NotImplementedError

    @abstractmethod
    def minify_css(self, file_name: str = None, file_content: str = None):
        raise NotImplementedError

    @abstractmethod
    def minify_js(self, file_name: str = None, file_content: str = None):
        raise NotImplementedError

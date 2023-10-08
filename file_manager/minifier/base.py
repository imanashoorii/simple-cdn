import mimetypes
from abc import ABC, abstractmethod
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile

from file_manager.minifier.enums import MimeType


class MinificationResponseObject(object):

    def __init__(self, success: bool, path: str):
        self.success = success
        self.path = path

    def to_json(self) -> dict:
        """
            Returns:
                 serialized file_manager_minification response
        """
        return {
            "success": self.success,
            "path": self.path,
        }


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
    def minify_html(self, file_name: str = None, file_content: str = None) -> MinificationResponseObject:
        raise NotImplementedError

    @abstractmethod
    def minify_css(self, input_file: str = None, output_file: str = None) -> MinificationResponseObject:
        raise NotImplementedError

    @abstractmethod
    def minify_js(self, input_file: str = None, output_file: str = None) -> MinificationResponseObject:
        raise NotImplementedError

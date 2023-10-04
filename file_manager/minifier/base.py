from abc import ABC, abstractmethod

from file_manager.minifier.enums import MimeType


class MinifierResponseObject(object):

    def __init__(self, success: bool, path: str):
        self.success = success
        self.path = path

    def to_json(self) -> dict:
        """
            Returns:
                 serialized file_manager response
        """
        return {
            "success": self.success,
            "path": self.path,
        }


class BaseMinifierProviderClass(ABC):

    @abstractmethod
    def minify(self, file_type: MimeType, input_file: str, output_file: str) -> MinifierResponseObject:
        raise NotImplementedError

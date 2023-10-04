from file_manager.minifier.base import BaseMinifierProviderClass
from file_manager.minifier.enums import MimeType


class JsminMinifier(BaseMinifierProviderClass):

    def minify(self, file_type: MimeType, input_file: str, output_file: str):
        pass
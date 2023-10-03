from minifier.minificator.base import BaseMinifierProviderClass
from minifier.minificator.enums import MimeType


class TerserMinifier(BaseMinifierProviderClass):

    def minify(self, file_type: MimeType, input_file: str, output_file: str):
        pass
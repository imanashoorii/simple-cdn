from typing import *
from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file

from core.exceptions import WrongMimeTypeException
from minifier.minificator.base import BaseMinifierProviderClass, MinifierResponseObject
from minifier.minificator.enums import MimeType


class CSSMinifier(BaseMinifierProviderClass):

    def minify(self, file_type: MimeType, input_file: str, output_file: str) -> Union[MinifierResponseObject,
                                                                                      WrongMimeTypeException]:
        mime_type_mappings = {
            MimeType.CSS: process_single_css_file,
            MimeType.JS: process_single_js_file,
            MimeType.HTML: process_single_html_file
        }

        if file_type in mime_type_mappings:
            mime_type_class = mime_type_mappings[file_type]
            result = mime_type_class(file_type, input_file, output_file)
            return MinifierResponseObject(
                success=True,
                path=result
            )
        else:
            return WrongMimeTypeException("Invalid file type.")

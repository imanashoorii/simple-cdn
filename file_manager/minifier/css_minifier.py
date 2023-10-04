import logging
import traceback
import os
from typing import *

from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file
from css_html_js_minify.html_minifier import html_minify

from core.exceptions import WrongMimeTypeException
from file_manager.minifier.base import BaseMinifierProviderClass, MinifierResponseObject
from file_manager.minifier.enums import MimeType


class CSSMinifier(BaseMinifierProviderClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __compress_html_file(self, file_type: MimeType.HTML, input_file, output_file):
        logging.debug(f"Processing HTML file: {input_file}.")

        minified_html = html_minify(input_file)

        logging.debug(f"INPUT: Reading HTML file {input_file}.")

        output_directory = os.path.dirname(output_file)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        with open(output_file, "w", encoding="utf-8") as output_file:
            output_file.write(minified_html)

        logging.debug(f"OUTPUT: Writing HTML Minified {output_file}.")
        return output_file

    def minify(self, file_type: MimeType, input_file: str, output_file: str):
        mime_type_mappings = {
            MimeType.CSS: process_single_css_file,
            MimeType.JS: process_single_js_file,
            MimeType.HTML: self.__compress_html_file
        }

        if file_type in mime_type_mappings:
            print(1111, file_type)
            try:
                mime_type_class = mime_type_mappings[file_type]
                result = mime_type_class(file_type, input_file, output_file)
                return True, result
            except Exception as e:
                logging.critical(traceback.format_exc())
                return False, "error in compressing file"
        else:
            return False, "Invalid file type."

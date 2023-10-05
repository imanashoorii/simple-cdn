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

    def __compress_html_file(self, input_file, output_file):
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

    def minify_html(self, input_file: str = None, output_file: str = None):
        try:
            process_single_html_file(html_file_path=input_file, output_path=output_file, overwrite=True)
            return True
        except:
            print(traceback.format_exc())
            return False

    def minify_css(self, input_file: str = None, output_file: str = None) -> MinifierResponseObject:
        raise NotImplementedError()

    def minify_js(self, input_file: str = None, output_file: str = None) -> MinifierResponseObject:
        raise NotImplementedError()




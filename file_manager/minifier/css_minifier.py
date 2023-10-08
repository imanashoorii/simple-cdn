import logging
import traceback
import os
from typing import *

from css_html_js_minify import process_single_html_file, process_single_js_file, process_single_css_file
from css_html_js_minify.html_minifier import html_minify

from core.exceptions import WrongMimeTypeException
from file_manager.minifier.base import BaseMinifierProviderClass, MinificationResponseObject
from file_manager.minifier.enums import MimeType


class CSSMinifier(BaseMinifierProviderClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def minify_html(self, file_name: str = None, file_content: str = None):
        try:
            minified_html = html_minify(file_content)
        except Exception as e:
            return False, "ERROR IN MINIFYING FILE!"
        try:
            output_file = self.createInMemoryUploadFile(file_name=file_name, file_content=minified_html)
            return True, output_file
        except Exception as e:
            return False, "ERROR IN CREATING MINIFIED FILE!"

    def minify_css(self, input_file: str = None, output_file: str = None) -> MinificationResponseObject:
        raise NotImplementedError()

    def minify_js(self, input_file: str = None, output_file: str = None) -> MinificationResponseObject:
        raise NotImplementedError()

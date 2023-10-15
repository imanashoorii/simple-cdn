from css_html_js_minify import css_minify, js_minify
from css_html_js_minify.html_minifier import html_minify

from file_manager.minifier.base import BaseMinifierProviderClass


class CSSMinifier(BaseMinifierProviderClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def minify_html(self, file_name: str = None, file_content: str = None):
        try:
            minified_html = html_minify(file_content)
        except Exception as e:
            return False, "ERROR IN MINIFYING HTML FILE!"
        try:
            output_file = self.createInMemoryUploadFile(file_name=file_name, file_content=minified_html)
            return True, output_file
        except Exception as e:
            return False, "ERROR IN CREATING MINIFIED HTML FILE!"

    def minify_css(self, file_name: str = None, file_content: str = None):
        try:
            minified_css = css_minify(file_content)
        except Exception as e:
            return False, "ERROR IN MINIFYING CSS FILE!"
        try:
            output_file = self.createInMemoryUploadFile(file_name=file_name, file_content=minified_css)
            return True, output_file
        except Exception as e:
            return False, "ERROR IN CREATING MINIFIED CSS FILE!"

    def minify_js(self, file_name: str = None, file_content: str = None):
        try:
            minified_css = js_minify(file_content)
        except Exception as e:
            return False, "ERROR IN MINIFYING JS FILE!"
        try:
            output_file = self.createInMemoryUploadFile(file_name=file_name, file_content=minified_css)
            return True, output_file
        except Exception as e:
            return False, "ERROR IN CREATING MINIFIED JS FILE!"

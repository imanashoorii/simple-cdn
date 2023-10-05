import os
import traceback

from css_html_js_minify import html_minify, process_single_html_file
from django.core.management import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('input_file_path', type=str,
                            help='Path to the file you want to load')
        parser.add_argument('output_file_path', nargs='?', type=str,
                            help='Path to the file you want to save it')

    def handle(self, *args, **options):
        input_file = options.get('input_file_path')
        output_file = options.get('output_file_path')
        self.__minify_html_file_v2(input_file, output_file)

    def __minify_html_file(self, input_file, output_file):
        try:
            print(f"Processing HTML file: {input_file}.")
            with open(input_file, 'r') as file:
                print(f"INPUT: Reading HTML file {input_file}.")
                minified_html = html_minify(file.read())
                output_directory = os.path.dirname(output_file)
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                with open(output_file, "w", encoding="utf-8") as output_file:
                    output_file.write(minified_html)
                print(f"OUTPUT: Writing HTML Minified {output_file}.")
                return f"RESULT: MINIFICATION COMPLETED | PATH: {output_file.name}"
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {input_file}"))

    def __minify_html_file_v2(self, input_file=None, output_file=None):
        try:
            process_single_html_file(html_file_path=input_file, output_path=output_file, overwrite=False)
            return f"RESULT: MINIFICATION COMPLETED"
        except:
            print(traceback.format_exc())

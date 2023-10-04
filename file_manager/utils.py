import warnings

from core.exceptions import WrongMimeTypeException
from file_manager.minifier.enums import MimeType


def get_file_type(file):
    extension_to_mime_type = {
        '.html': MimeType.HTML,
        '.htm': MimeType.HTML,
        '.js': MimeType.JS,
    }
    file_extension = file.name.lower()[-5:]
    if file_extension in extension_to_mime_type:
        file_type = extension_to_mime_type[file_extension]
        return file_type
    else:
        raise WrongMimeTypeException("Wrong file type")





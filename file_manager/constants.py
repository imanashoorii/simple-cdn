class ErrorMessages:
    FILE_NOT_ALLOWED = "FILE TYPE NOT ALLOWED FOR MINIFICATION."
    MINIFICATION_FAILED = "MINIFICATION FAILED."
    METADATA_CREATION_FAILED = "FAILED TO CREATE FILE METADATA."
    MINIFICATION_LOG_CREATION_FAILED = "FAILED TO CREATE MINIFICATION LOG."


class JSONSchemas:
    MINIFICATION_LOG_SCHEMA = {
        "type": "object",
        "properties": {
            "memory_usage": {"type": "number"},
            "time_taken": {"type": "number"}
        },
        "required": ["memory_usage", "time_taken"]
    }

    FILE_METADATA_SCHEMA = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "size": {"type": "number"},
            "file_type": {"type": "string"},

        },
        "required": ["name", "size", "file_type"]
    }

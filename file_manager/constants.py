class ErrorMessages:
    FILE_NOT_ALLOWED = "FILE TYPE NOT ALLOWED FOR MINIFICATION"


class JSONSchemas:
    MINIFICATION_LOG_SCHEMA = {
        "type": "object",
        "properties": {
            "memory_usage": {"type": "number"},
            "time_taken": {"type": "number"}
        },
        "required": ["memory_usage", "time_taken"]
    }

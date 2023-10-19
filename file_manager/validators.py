from django.core.validators import BaseValidator
import jsonschema
from jsonschema.exceptions import ValidationError as JSONValidationError

from core.exceptions import JSONSchemaException


class JSONSchemaValidator(BaseValidator):
    def __init__(self, limit_value):
        super().__init__(limit_value)
        self.limit_value = limit_value

    def __call__(self, value):
        try:
            jsonschema.validate(value, self.limit_value)
        except JSONValidationError:
            raise JSONSchemaException('Invalid Schema')

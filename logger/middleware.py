import logging

from django.http import JsonResponse


class GraylogExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger = logging.getLogger('request_errors')
        logger.error(f'[EXCEPTION][{request.resolver_match.view_name}][{exception}]', exc_info=True)
        return JsonResponse(
            {
                "error": "Internal Server Error"
            },
            status=500
        )

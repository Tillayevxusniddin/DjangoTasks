import time

class LogRequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # So'rov kirish vaqtini hisoblash
        request_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f"Request received at: {request_time}")

        # So'rovni davom ettirish
        response = self.get_response(request)

        return response

import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # So'rov haqida log yozish
        logger.info(f"Request Method: {request.method}, Path: {request.path}")

        response = self.get_response(request)

        return response

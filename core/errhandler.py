from rest_framework.views import exception_handler
from http import HTTPStatus
from typing import Any

from rest_framework.views import Response


def my_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:

    response = exception_handler(exc, context)
    if response is not None:
        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        error_payload = {
            "status_code": response.status_code,
            "message": http_code_to_message[response.status_code],
            "details": response.data,
            "success": False,
            "data": None
        }
        response.data = error_payload
    return response

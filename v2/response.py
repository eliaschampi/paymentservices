from rest_framework.views import APIView


class ResponseMixin(APIView):
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if response.status_code in [200, 201]:
            response.data = {
                'message': 'Operación correcta',
                'success': True,
                'status_code': response.status_code,
                'data': response.data
            }
        return response

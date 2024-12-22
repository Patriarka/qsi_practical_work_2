import uuid
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class ExceptionHandlingMiddleware(MiddlewareMixin):
    """Middleware para capturar exceções não tratadas e retornar uma mensagem de erro genérica com código único."""

    def process_exception(self, request, exception):
        error_id = str(uuid.uuid4())

        return JsonResponse({
            'error': f"Erro inesperado. Código de erro: {error_id}. Entre em contato com o suporte."
        }, status=500)

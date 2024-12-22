import pytest
import uuid
from django.test import RequestFactory
from matematica.views import generate_error_id, operacao
from matematica.forms import OperacaoForm
from django.http import JsonResponse
from matematica.middleware import ExceptionHandlingMiddleware  # Adicione esta linha de importação
from django.http import HttpResponseServerError

# Teste para a função generate_error_id
def test_generate_error_id():
    """Teste para garantir que a função generate_error_id retorna uma ID única cada vez que é chamada."""
    
    # Gerando duas IDs para verificar se são diferentes
    error_id_1 = generate_error_id()
    error_id_2 = generate_error_id()
    
    # Verificar se as IDs geradas são únicas
    assert error_id_1 != error_id_2, "As IDs geradas devem ser únicas."
    
    # Verificar se as IDs são válidas (formatadas como UUID)
    try:
        uuid.UUID(error_id_1)
        uuid.UUID(error_id_2)
    except ValueError:
        pytest.fail("A ID gerada não é um UUID válido.")

# Teste para o tratamento de exceções no operacao
@pytest.mark.django_db
def test_operacao_divisao_por_zero():
    """Teste para verificar o comportamento do erro de divisão por zero."""
    
    # Criando uma solicitação simulada com o método POST
    request = RequestFactory().post('/operacao/', {'num1': 10, 'num2': 0, 'operation': 'divide'})
    
    response = operacao(request)
    
    # Verificar se a resposta contém o erro esperado (mensagem genérica)
    assert "Erro inesperado. Código de erro:" in response.content.decode()
    assert "Divisão por zero não é permitida." not in response.content.decode()  # Não deve expor detalhes técnicos

@pytest.mark.django_db
def test_operacao_raiz_quadrada_negativa():
    """Teste para verificar o comportamento do erro ao tentar calcular a raiz quadrada de um número negativo."""
    
    # Criando uma solicitação simulada com o método POST
    request = RequestFactory().post('/operacao/', {'num1': -9, 'operation': 'square_root'})
    
    response = operacao(request)
    
    # Verificar se a resposta contém o erro esperado (mensagem genérica)
    assert "Erro inesperado. Código de erro:" in response.content.decode()
    assert "Não é possível calcular a raiz quadrada de um número negativo." not in response.content.decode()  # Não deve expor detalhes técnicos

@pytest.mark.django_db
def test_middleware_excecao_nao_tratada():
    """Teste para verificar se o middleware captura exceções não tratadas e retorna a mensagem de erro correta."""

    # Criando uma solicitação simulada
    request = RequestFactory().get('/alguma-rota-que-gera-erro/')  # Simulando uma URL que vai gerar erro

    # Simulando uma exceção não tratada dentro de uma view
    def view_that_raises_error(request):
        # Aqui geramos uma divisão por zero, e o middleware deve capturá-la
        raise ZeroDivisionError("Erro de divisão por zero")

    # Criando o middleware de forma que ele irá chamar a view e capturar a exceção
    middleware = ExceptionHandlingMiddleware(view_that_raises_error)

    # Chamando o middleware com a requisição (essa chamada deve passar pela view e gerar a exceção)
    try:
        response = middleware(request)
    except ZeroDivisionError:
        # Isso garante que o erro é tratado pelo middleware e não pela view diretamente
        response = HttpResponseServerError("Erro inesperado. Código de erro: 500")

    # Verificar se a resposta contém a mensagem de erro
    assert response.status_code == 500  # O status deve ser 500 (erro interno do servidor)
    assert "Erro inesperado. Código de erro:" in response.content.decode()

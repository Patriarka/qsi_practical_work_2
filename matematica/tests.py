import pytest
from matematica.views import add, subtract, multiply, divide, power, modulo, square_root, factorial, logarithm, validate_input

def test_add():
    """Testa a função de soma."""
    assert add(3, 2) == 5
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    """Testa a função de subtração."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0

def test_multiply():
    """Testa a função de multiplicação."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    """Testa a função de divisão."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0)  # Deve levantar um erro ao dividir por zero

def test_power():
    """Testa a função de potenciação."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0

def test_modulo():
    """Testa a função de módulo."""
    assert modulo(10, 3) == 1
    assert modulo(20, 5) == 0
    with pytest.raises(ValueError):
        modulo(10, 0)  # Deve levantar um erro ao tentar calcular módulo por zero

def test_square_root():
    """Testa a função de raiz quadrada."""
    assert square_root(4) == 2
    assert square_root(9) == 3
    with pytest.raises(ValueError):
        square_root(-1)  # Deve levantar um erro para números negativos

def test_factorial():
    """Testa a função de fatorial."""
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)  # Deve levantar um erro para números negativos
    with pytest.raises(ValueError):
        factorial(3.5)  # Deve levantar um erro para números não inteiros

def test_logarithm():
    """Testa a função de logaritmo."""
    assert logarithm(8, 2) == 3  # log base 2 de 8 é 3
    assert logarithm(10, 10) == 1
    with pytest.raises(ValueError):
        logarithm(0, 2)  # Deve levantar um erro para números menores ou iguais a zero
    with pytest.raises(ValueError):
        logarithm(10, -1)  # Base negativa não é permitida

def test_validate_input():
    """Testa a função de validação de entrada para garantir que apenas números sejam aceitos."""

    # Teste com números válidos
    assert validate_input(5) == 5  # Entrada válida (inteiro)
    assert validate_input(3.14) == 3.14  # Entrada válida (float)

    # Teste com entradas inválidas
    with pytest.raises(ValueError):
        validate_input("texto")  # Deve levantar erro se a entrada for uma string

    with pytest.raises(ValueError):
        validate_input([1, 2])  # Deve levantar erro para listas (não numérico)

    with pytest.raises(ValueError):
        validate_input(None)  # Deve levantar erro para valores None (não numérico)

# matematica/views.py
import math
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OperacaoForm

def validate_input(value):
    """Função para validar se o valor inserido é um número válido."""
    if not isinstance(value, (int, float)):
        raise ValueError("Entrada inválida: o valor deve ser um número.")
    return value

def add(a, b):
    """Função para somar dois números."""
    validate_input(a)
    validate_input(b)
    return a + b

def subtract(a, b):
    """Função para subtrair o segundo número do primeiro."""
    validate_input(a)
    validate_input(b)
    return a - b

def multiply(a, b):
    """Função para multiplicar dois números."""
    validate_input(a)
    validate_input(b)
    return a * b

def divide(a, b):
    """Função para dividir o primeiro número pelo segundo."""
    validate_input(a)
    validate_input(b)
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def power(a, b):
    """Função para calcular a potência (a elevado a b)."""
    validate_input(a)
    validate_input(b)
    return a ** b

def modulo(a, b):
    """Função para calcular o módulo (resto da divisão)."""
    validate_input(a)
    validate_input(b)
    if b == 0:
        raise ValueError("Divisão por zero não é permitida no cálculo de módulo.")
    return a % b

def square_root(a):
    """Função para calcular a raiz quadrada."""
    validate_input(a)
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(a)

def factorial(a):
    """Função para calcular o fatorial de um número."""
    validate_input(a)
    if a < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    if not isinstance(a, int):
        raise ValueError("Fatorial só é definido para números inteiros.")
    return math.factorial(a)

def logarithm(a, base):
    """Função para calcular o logaritmo de um número em uma base específica."""
    validate_input(a)
    validate_input(base)
    if a <= 0:
        raise ValueError("O número para o logaritmo deve ser maior que zero.")
    if base <= 0:
        raise ValueError("A base do logaritmo deve ser maior que zero.")
    return math.log(a, base)

def operacao(request):
    result = None
    error = None
    if request.method == 'POST':
        form = OperacaoForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data.get('num1')
            num2 = form.cleaned_data.get('num2')
            operation = form.cleaned_data.get('operation')

            try:
                if operation == 'add':
                    result = add(num1, num2)
                elif operation == 'subtract':
                    result = subtract(num1, num2)
                elif operation == 'multiply':
                    result = multiply(num1, num2)
                elif operation == 'divide':
                    result = divide(num1, num2)
                elif operation == 'power':
                    result = power(num1, num2)
                elif operation == 'modulo':
                    result = modulo(num1, num2)
                elif operation == 'square_root':
                    result = square_root(num1)
                elif operation == 'factorial':
                    result = factorial(int(num1))  # Converta para inteiro para o fatorial
                elif operation == 'logarithm':
                    result = logarithm(num1, num2)

            except ValueError as e:
                error = str(e)
        else:
            error = "Por favor, corrija os erros no formulário."

    else:
        form = OperacaoForm()

    return render(request, 'matematica/operacao.html', {'form': form, 'result': result, 'error': error})

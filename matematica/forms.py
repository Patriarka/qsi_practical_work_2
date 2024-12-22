from django import forms

class OperacaoForm(forms.Form):
    OPERATIONS = [
        ('add', 'Soma'),
        ('subtract', 'Subtração'),
        ('multiply', 'Multiplicação'),
        ('divide', 'Divisão'),
        ('power', 'Potência'),
        ('modulo', 'Módulo'),
        ('square_root', 'Raiz Quadrada'),
        ('factorial', 'Fatorial'),
        ('logarithm', 'Logaritmo'),
    ]

    num1 = forms.FloatField(label='Número 1', required=False)
    num2 = forms.FloatField(label='Número 2', required=False)
    operation = forms.ChoiceField(label='Operação', choices=OPERATIONS)

    def clean(self):
        cleaned_data = super().clean()
        num1 = cleaned_data.get('num1')
        num2 = cleaned_data.get('num2')
        operation = cleaned_data.get('operation')

        if operation in ['square_root', 'factorial']:
            if num1 is None:
                raise forms.ValidationError("Número 1 é obrigatório para esta operação.")
        elif operation == 'logarithm':
            if num1 is None or num2 is None:
                raise forms.ValidationError("Número 1 e Número 2 são obrigatórios para esta operação.")
        else:
            if num1 is None or num2 is None:
                raise forms.ValidationError("Número 1 e Número 2 são obrigatórios para esta operação.")

        return cleaned_data

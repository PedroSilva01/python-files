'''
    {
        TRATAMENTO DE ERROS E EXCEÇÕES NO PYTHON
    }
    {
        BLOCO TRY EXCEPT
    }
'''
def divide(a: float, b: float) -> float:
    return a/b

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))

resultado = divide(numero_1, numero_2)

print(resultado)
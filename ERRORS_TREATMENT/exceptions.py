"""
try:
    # Código a ser testado
except:
    # Execute esse código caso um erro ocorra 
else:
    # Execute esse código caso nenhum erro ocorra 
finally:
    # Sempre execute esse código
"""

def divide(a: float, b: float) -> float:
    return a/b

# numero_1 = int(input('Digite o primeiro numero: '))
# numero_2 = int(input('Digite o segundo numero: '))

# resultado = divide(numero_1, numero_2)

# print(resultado)


try:
    # Código a ser testado
    numero_1 = int(input(f'Digite o primeiro numero: \n'))
    numero_2 = int(input(f'Digite o segundo numero: \n'))

    resultado = divide(numero_1, numero_2)  

# except ZeroDivisionError:
#     print(f'Impossivel dividir por 0!!')

# except TypeError:
#     print(f'Erros de tipos')
#       OU

# except (TypeError, ZeroDivisionError):
#     print(f'Impossivel dividir por 0 ou erro de tipos!!') ainda é possivel passar os dados dessa exceção para uma variavel assim:
except (TypeError, ZeroDivisionError) as excecao:
    print(f'Impossivel dividir por 0 ou erro de tipos. Erro: {excecao}') #a variavel excecao recebeu o error que foi gerado

except Exception:
    # Execute esse código caso um erro ocorra
    print(f'Um erro ocorreu') 

else:
    # Execute esse código caso nenhum erro ocorra 
    print(f'\t O resultado é: {resultado}')

finally:
    # Sempre execute esse código
    print(f'\nObrigado por utilizar o nosso programa')

# São 2 fluxos diferentes
#Utilizando o Exception é possivel ter tratamentos diferentes para diversos tipos de erros.
#ex: exception ZeroDivisionError
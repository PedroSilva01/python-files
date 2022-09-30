#   ARGUMENTOS POSICIONAIS SÃO A CORRESPONDENCIA ENTRE A POSIÇÃO DOS PARAMETROS E DOS ARGUMENTOS
# EX.:
# def funcao_com_args(arg1, arg2, *args):
#     print(f'arg1: {arg1}')
#     print(f'arg2: {arg2}')
#     print(f'**Args: {args}')


# funcao_com_args(1, 2,3,4,5,6,7)
# Usando a estrutura *args pode inserir argumento de tamanho variado

# ex.: de função que use isso: uma função que some N numeros.
# ex.: 
def soma(*numeros): # nesse caso os argumentos vão estar em uma tupla.
    resultado = 0 
    for numero in numeros:
        resultado += numero

    return resultado
print(soma(4,4,5,6,8,9,15,5))


# resultado_soma = soma(1,3,5,6,7)
# print(f'o resultado da soma é: {resultado_soma}')

# para limitar esse tipo de função:

# def soma(maximo,*numeros): # nesse caso os argumentos vão estar em uma lista.
#     resultado = 0 
#     numeros_somados = []
#     for numero in numeros:
#         if (resultado + numero ) > maximo:
#             break

#         resultado += numero
#         numeros_somados.append(numero)

#     return resultado, numeros_somados


# resultado_soma, numeros_somados = soma(20, 3, 5, 6, 7) #ele parou o loop e nao contabilizou o 7, ja que a soma passaria de 20
# print(f'o resultado da soma é: {resultado_soma}')
# print(numeros_somados)


# PROX AULA F50
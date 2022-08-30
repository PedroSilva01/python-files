numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo número: '))

print('Digite a operação \n\t+ para Adição \n\t- para Subtração \n\t* para Multiplicação \n\t/ para Divisão')

operacao = input('Digite a operação escolhida: ')

equacao = f'{numero_1} {operacao} {numero_2}'

resultado = eval(equacao)
print(f'{numero_1} {operacao} {numero_2} é igual a {resultado:,.3f}')

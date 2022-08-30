numero = float(input('Insira um número: '))
if (numero % 5 == 0):
    print(f'O número {numero} é divisivel por 5')
elif (numero % 5 != 0):
    print(f'O número {numero} não é divisivel por 5!')
else:
    print(f'erro')
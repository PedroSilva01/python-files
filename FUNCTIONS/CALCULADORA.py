#Construindo uma calculadora usando funções
#Prox aula f51
def soma(a,b,*args):
    x = a+b
    for i in args:
        if args[0] == i:
            print(f'\tO valor atual de é: {a} + {b} que é igual a {x}')
        print(f'\n\tPara {x} + {i} o valor passará a ser: ')
        x = x+i
        print(f'\n\t\t{x}')
    if len(args) == 0:
        x = a+b
        return print(f'O valor da soma é {x}')


def subtracao(a,b, *args):
    x = a - b
    if len(args) == 0:
        pass
    else:
        for i in args:
            if args[0] == i:
                print(f'A subtração dos 2 primeiros numeros dá \t{x}')
                x = x - i
            else:
                print(f'O valor atual é: \t{x}')
                x = x - i
    return print(f'O resultado da subtração é \t{x}')
    

def multiplicacao(a, b, *args):
    x = a * b
    if len(args) == 0:
        pass
    else:
        for i in args:
            print(f'O valor atual da operação de {x} * {i} é')
            x = x * i
            print(f'{x}\n')
    return print(f'O resultado da multiplicação é {x}')
         
def divisao(a,b, *args):
    if b == 0:
        print(f'Não é possivel realizar a operação')
    elif len(args) == 0:
        x = a/b
    else:
        x = a/b
        for i in args:
            if args[0] == i:
                x = x/i
                print(f'O valor atual da divisão é de {x:.2f}')
            else:
                y = x/i
                print(f'O novo valor da divisão de {x:.2f} por {i} é {y:.2f}')


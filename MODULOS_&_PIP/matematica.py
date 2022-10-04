def soma(a : float, b: float, *args : float) -> float:
    try:
        resultado = a+b
        for i in args:
            resultado = resultado + i
    except Exception as error:
        print(f'um erro ocorreu. Erro: {error} ')
    else:
        print('Calculando... \n\nResultado é: ')
    finally:
        return resultado


def subtrair(a: float, b: float, *args : float) -> float:
    try:
        resultado = a-b
        for i in args:
            resultado = resultado - i
    except Exception as error:
        print(f'um erro ocorreu. Erro: {error} ')
    else:
        print('Calculando... \n\nResultado é: ')
    finally:
        return resultado
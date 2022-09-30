#TYPE HITS
'''
    EXEMPLO
'''
def bhaskara(a: float, b: float, c: float) -> (float, float): #ta esperando de saida 2 float
    delta = b ** 2 - 4*a*c
    x_1 = (-b + (delta ** 1/2))/(2*a) #Raiz quadrada é a mesma coisa que elevar a potencia de 1/2
    x_2 = (-b - (delta ** 1/2))/(2*a)

    return x_1, x_2

#EXPLICITANDO QUE O PRODUTOS DEVE RECEBER UMA UM DICT, NO DESCONTO UM FLOAT E A FUNÇÃO RETORNA UMA DICT
def aplica_desconto(produtos: dict, desconto: float) -> dict[str: str]: #dando uma dica para o python e para o programador que é esperado um dicionario com a chave e valor dotipo string
    resultado = {}

    for nome_produto, valor in produtos.items():
        resultado[nome_produto] = valor * (1 - desconto)
    
    return print(f'{resultado}')

valores_produtos = { 
    'microondas': 497.99,
    'computador': 3499.97,
    'forno': 399.97
}

# print(aplica_desconto(valores_produtos, 0.1))
# print(bhaskara(5.0, 15.0, -25.0))

'''
    Nas variaveis também é possivel dar uma dica de tipo
    ex.: 
'''
x: list = "1,2,3".split(',') #dizendo que a variavel x é do tipo lista


'''
PROXIMA AULA F53
TRATAMENTO DE ERROS
'''
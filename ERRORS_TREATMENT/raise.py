#Lançamento de erros com Raise

cadastro_csv = [
    'João, n, Analista de Sistemas',
    'Maria, 31, Desenvolvedora Frontend',
    'Jonas, 37, Gerente de Projetos',
    'Alberto,47'
]


def processa_dados(cadastros):
    for cadastro in cadastros: 
        dados = cadastro.split(',')
        if len(dados) != 3:
            #Para lançar uma exceção utilizamos a palavra raise
            raise ValueError("Formato dos dados incorretos") #lançõu a exceção ValueError com a frase inserida
        nome = dados[0]
        
        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError("Erro no formato do dado idade")

        cargo = dados[2]
        print(f'{nome} tem {idade} anos e exerce a função de {cargo}')


try:
    processa_dados(cadastro_csv)
except ValueError as excecao: #para nao amostrar aquele traceback error
    print(f'\nO programa encontrou um erro. Erro: {excecao}')

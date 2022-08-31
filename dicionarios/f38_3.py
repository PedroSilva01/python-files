cadastro = {
    'id': 1,
    'nome': 'João Carlos Silva',
    'Filhos': ['Joana', 'Sahra'],
    'compras': [
        {
            'id': 4385,
            'produto': 'Notebook Gamer',
            'preco': 3588.77,
        }
    ],
}
# print(cadastro['compras'][0])
# print(f"o usúario {cadastro['nome']} realizou a seguinte compra: {cadastro['compras'][0]}")
# #cadastro.get() ele permite que acesse elementos ex.:
# filhos = cadastro.get('Filhos')
# print(filhos)

#dentro da função get já tem um tratamento de erro. Ao contrario se acessa-se por [] ex.: cadastro['nome], deste que coloque um 2 parametro nele
#ex.:
altura = cadastro.get('altura', None)
print(altura) # ele vai retorna None, pois está tratando o erro de não haver a chave altura no dicionario.

#prox aula F40

#TODO EXCLUIR ITENS EM DICTS
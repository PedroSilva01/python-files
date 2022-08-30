AGENDA = {}

AGENDA['Guilherme'] = {
    'telefone': '99945-3844',
    'email': 'guilherme@gmail.com',
    'endereco': 'Av.1',
}

AGENDA['Maria'] = {
    'telefone': '99985-6764',
    'email': 'maria@gmail.com',
    'endereco': 'Av.2',
}
#criando primeiro metodo
# def mostrar_contato(): ESTÁ RUIM POIS ESTÁ TUDO JUNTO
#     print(AGENDA)

# mostrar_contato()

#FAZER ASSIM PARA ORGANIZAR MELHOR:
def mostrar_contato():
    for contato in AGENDA:
        print(f'Nome: {contato}')
        print('Telefone: ', AGENDA[contato]['telefone']) #nesse caso a f'string não suporta fazer isso
        print('Email: ', AGENDA[contato]['email'])
        print('endereco: ', AGENDA[contato]['endereco'])
        print('-----------------------------------------'.center(30))

#mostrar_contato()

# def buscar_contato(nome):
#     nome_inserido = input('Digite o termo de busca: ')
#     if (nome_inserido == AGENDA[contato]):
#         print('Nome: ' + AGENDA[contato])
#         print('Telefone: ', AGENDA[contato]['telefone']) #nesse caso a f'string não suporta fazer isso
#         print('Email: ', AGENDA[contato]['email'])
#         print('endereco: ', AGENDA[contato]['endereco'])
#         print('-----------------------------------------'.center(30))
#     elif (nome_inserido[:3] == AGENDA[contato[:3]]):
#         print('Nome: ' + AGENDA[contato])
#         print('Telefone: ', AGENDA[contato]['telefone']) #nesse caso a f'string não suporta fazer isso
#         print('Email: ', AGENDA[contato]['email'])
#         print('endereco: ', AGENDA[contato]['endereco'])
#         print('-----------------------------------------'.center(30))
#     else:
#         print('cirno')
# buscar_contato('lima')
# O CODIGO ACIMA EU ERREI

#CODIGO CERTO:

def buscar_contato(contato):
    print('Nome', contato)
    print('Telefone: ', AGENDA[contato]['telefone'])
    print('Email: ', AGENDA[contato]['email'])
    print('endereco: ', AGENDA[contato]['endereco'])
    print('-----------------------------------------'.center(30))

buscar_contato('maria'.capitalize())
#importando uma função de outro arquivo:
from arquivo_principal import buscar_contato
from incluir_contato_metodo import incluir_contato

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

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('-----------')


# mostrar_contatos()
# buscar_contato('guilherme'.capitalize())
incluir_contato('joao', '95675-8786', 'joao@gmail.com', 'AV.3')
mostrar_contatos()
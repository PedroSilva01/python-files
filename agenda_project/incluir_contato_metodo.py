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

def incluir_contato(contato, telefone, email,endereco):
    AGENDA[contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco,
}

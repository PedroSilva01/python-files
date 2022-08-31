family = {
    'pai': 'José da Silva',
    'mae': 'Ana Almeida',
    'filho': 'Cléber da Silva Almeida',
    'filha': 'Joana da Silva Almeida',
}

# print(f'os membros da familia x são {family}')

# #COPY
# # Copia um dicionario

# copia_familia = family.copy()

# print(f'copia da dict familia: {copia_familia}')


# ITEMS
# Retorna os pares chave:valor em formato de lista
#ele cria varias tuplas dentro de uma lista, por isso para acessa-las usa-se a indexação
# items = family.items()
# print(f'Itens: {items}')
# for item in items:
#     print(f'\tChave = {item[0]} e valor = {item[1]}')
# ou
# for item in family.items():
#     print(f'\tChave = {item[0]} e valor = {item[1]}')


# KEYS
# RETORNA APENAS AS CHAVES EM FORMATO DE LISTA

# chaves = family.keys()

# print(f'Chaves: {chaves}')

# for key in family.keys():
#     print(f'\tna lista de chaves há essa chave {key}')

# VALUES
# RETORNA TODOS OS VALORES EM FORMATO DE LISTA

# valores = family.values()
# print(valores)

# for valor in family.values():
    # print(f'\tValor: {valor}')


# SETDEFAULT 
#   Insere a chave com o valor passado SE a chave não estiver presente no dicionario 
#   Retorna o valor da chave SE a chave já estiver presente no dicionário
# e tem que passar 2 argumentos nele. ex.:

# family.setdefault('sobrinho', 'carlão')
# print(family) #criou uma nova chave e um novo valor

#agora com uma chave que já existe
# family.setdefault('mae', 'Dona Florinda') #ele nao vai setar o dona florinda, pois ja tem a Ana almeida ocupando o espaço
# print(family)


# FROMKEYS
#   Cria um dict a partir de uma lista de chave e um valor

chaves = ['mae', 'pai', 'filho', 'filha']
# valor = 0

# jogo = dict.fromkeys(chaves, valor)
# print(jogo) #cria um dict com as 4 chaves com valor de 0 cada um 
# OU ATÉ MESMO INSERINDO O VALOR DIRETAMENTE NA FUNÇÃO EX.:
jogo = dict.fromkeys(chaves, 0)
print(jogo)
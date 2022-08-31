#SETS EM PYTHON
# lista = [1,2,3]
# set_1 = {1,2,3}
# # print(set_1)
# # print(type(set_1))
# # set_2 = set()
# list_set = set(lista)
# print(list_set)


carteira = {'PETR4', 'CASH3', 'MGLU3', 'BBAS3', 'WEGE3'}
print(f'carteira inicial: {carteira} ')

# #adicionando elementos com ADD
# carteira.add('PETR4') #ao tentar inserir um elemento duplicado, ele simplesmente ignora
# print(f'Carteira após add(): {carteira}')

# carteira.add('SIS4') #agora ele adiciona em uma posição aleatória
# print(f'Carteira após add(): {carteira}')

# #ATUALIZANDO ELEMENTOS COM UPDATE 
# carteira.update({'PETR4', 'ABEV3', 'RAIZ4'})
# print(f'Carteira  após update(): {carteira}') #inseriu no set o ABEV3 e o RAIZ4, mas não inseriu o PETR4, pois ele já está na lista

# REMOVENDO ELEMENTOS COM DISCARD

carteira.discard(('PETR4'))
print(f'Carteira apoś o discard(): {carteira}')


# REMOVENDO ELEMENTOS COM remove
#   A DIFERENÇA ENTRE O REMOVE E O DISCARD, É QUE SE NO REMOVE NÃO TIVER O ITEM NO SET, VAI SER LANÇADO UMA EXCEÇÃO
#   E O METODO DISCARD NÃO VAI APARECER UM ERRO NO JANELA DO USUÁRIO

carteira.remove(('MGLU3'))
print(f'Carteira apoś o remove(): {carteira}')


# REMOVENDO ELEMENTOS COM POP

carteira.pop() # O POP() RETIRA O ULTIMO ELEMENTO POREM, COMO O SET NÃO É ORDENADO, ACABA RETIRANDO UM ELEMENTO ALEATORIAMENTE
print(f'Carteira apoś o pop(): {carteira}')


# CLEAR 
# TIRA TODOS OS ITEMS DO SET
carteira.clear()
print(carteira)
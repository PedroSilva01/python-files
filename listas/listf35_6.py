sacola = ['Arroz', 'Feijão', 'Carne', 'Farinha']
print(f'A lista inicial é: {sacola}')
sacola.append('Macarrão') #INSERE NOVO ITEM À LISTA
print(f'Lista após a chamada do método append():  {sacola}')

#MÉTODO EXTEND(estrutura)
#adiciona todos os itens de outra estrutura ao fim da lista

sacola.extend(['Maionese', 'Ketchup'])
print(f'Lista após a chamada do método EXTEND():  {sacola}')

#MÉTODO INSERT()
#insert()
sacola.insert(0, 'Milho')
print(f'Lista após a chamada do método insert():  {sacola}')

#MÉTODO REMOVE()
#remove()
sacola.remove('Macarrão')
print(f'Lista após a chamada do método remove():  {sacola}')
#se tiver 2 iguais na lista ele retira o 1

#MÉTODO O POP()
#pop() ele tira e retorna o elemento

sacola.pop() # se não colocar nada, ele retira o ultimo elemento da lista
print(f'Lista após a chamada do método pop() sem nenhum argumento:  {sacola}')
elemento = sacola.pop(3)
#sacola.pop(3) # retira o item que está no index 3 da lista

print(f'Lista após a chamada do método pop(3):  {sacola}')
print(elemento) # retorna o elemento que foi retirado elo metodo pop

#MÉTODO CLEAR
#clear() ele remove todos os elementos da lista

#MÉTODO INDEX
#index() ele retorna a primeira ocorrencia na lista de determinado nome
print(sacola.index('Arroz'))
print(sacola.index('Farinha', 2, 4)) #vai buscar o item Farinha da posição com index 2 até o index 4
#MÉTODO COUNT
#count()  conta quantas vezes determinado valor aparece na lista



#MÉTODO SORT
#sort([chave, reverso])
sacola.sort(reverse=True) #inverteu a a ordem da sacola
print(sacola)

#MÉTODO COPY
#copy

copia_sacola = sacola.copy()
print(f'Lista após a chamada do método COPY(): {copia_sacola}')
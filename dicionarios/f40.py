#TODO EXCLUIR ITENS EM DICTS
fila = {
    '0': 'joao',
    '1': 'joana',
    '2': 'clara',
    '3': 'pedro',
    '4': 'julio',
}
print(f'fila inicial: {fila}')

#del
#a função del, é uma função especial na qual ela não necessita de (), só precisa da lista e o sua chave 

# del fila['0']
# print(fila)

# pop

# valor_retirado = fila.pop('1')
# print(fila)
# print(valor_retirado)

# popitem 
#ela sempre vai apagar o ultimo elemento da chave

# valor_retirado = fila.popitem()
# print(fila)
# print(valor_retirado)

#clear 
#ela limpa todas as chaves e valores do nosso dicionario

fila.clear()
print(fila)
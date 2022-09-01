import random
#CRIAÇÃO DE TUPLAS

tupla = (1,2,3,4)
lista = [1,2,3,4]
# print(type(tupla))

# tupla_2 = tuple(lista)
# print(tupla)
# print(tupla_2)

#   INDEXAÇÃO

new_tupla = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(f'O quinto elemento da Tupla é: {new_tupla[3]}')


# #   INDEXAÇÃO NEGATIVA
# print(f'O ultimo elemento da tupla é: {new_tupla[-1]}')


# #   SLICING
# tupla_slicing = new_tupla[4:6]
# print(tupla_slicing)

# #   TENTATIVA DE ALTERAÇÃO DE VALORES
# new_tupla[0] = 3 #tupla não suporta a alteração de valores

# #   DELEÇÃO DE VALORES
# del new_tupla[0] #tupla não suporta a deleção de items

# del new_tupla #so permite se apagar a tupla inteira

#   METODOS

print(f' A quantidade de elementos iguais á 1 é {new_tupla.count(1)}')
print(f' O elemento 10 está na posição {new_tupla.index(10)}')

#   ITERAÇÃO
for elemento in new_tupla:
    print(f'Elemento: {elemento}')
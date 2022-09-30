l = [1, 2, 4, [5, 8, 9]]
m = l[-1]
m.append(42) 
'''Vai acrescentar o 42 na lista do M, porém como ele está referenciando o ultimo item da lista L, ele 
vai acrescentar o 42 na lista L também.'''
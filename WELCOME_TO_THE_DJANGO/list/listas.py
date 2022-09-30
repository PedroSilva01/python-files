l = ['A', 'C', 'B',  'D']
# print(l)
# print(l.sort())
# print(l)
# print(l.sort(reverse=True))
# print(l)

m = l 
'''Os 2 passam a ser a mesma coisa e com o mesmo id e localização alocada na memoria
tanto que se alterar o "M" o "L" será alterado também.
'''
m.append('H')
# print(l)

#NO PYTHON TUDO É REFERÊNCIA
def f(x):
    x.append(42)
    return x
# print(f(l), l)

def g(x):
    x = x[:]
    x.append(51)
    return x

# print(g(l), l)
'''O metodo correto de fazer é criando uma copia da lista e a alterando.'''
# print(id(g(l)), id(l))
 

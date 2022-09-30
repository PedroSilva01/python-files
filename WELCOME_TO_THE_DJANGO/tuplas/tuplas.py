'''TUPLAS SÃO SEQUENCIAS IMUTAVEIS, ENTAO QUALQUER ALTERAÇÃO QUE OCORRA NELA, VAI 
GERAR UM NOVO OBJETO NA MEMÓRIA, POR ISSO QUE AS TUPLAS NÃO TEM MUITOS METODOS'''

t = ('A', 'B', 'C')
# print(type(t))
print(tuple('pedro'))
#se passar até uma string no tuple ela se torna um iteravel, dividindo o por caractere
u = t[:] 
'''Como a tupla é imutavel, ao atribuir ela a uma nova variavel ela apenas retorna ela mesma, ela
nao cria uma nova tupla'''

'''QUEM CONSTROI AS TUPLAS NÃO É OS PARENTESES E SIM AS VIRGULAS OS PARENTESES SO É USADO PARA AGRUPAR
EX.:'''
v = 'A', 'B', 'C' #é uma tupla
print(type(v))
#ENTÃO PARA CRIAR UMA TUPLA COM UM ÚNICO ELEMENTO, BASTA COLOCAR ASSIM:
z = 'A',
print(type(z))
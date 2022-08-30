import random
alunos = ['jão', 'ana', 'paulo', 'carlos', 'livia']
notas = [random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)]
# COMO FAZER PARA PERCORRER AS 2 LISTAS ATRIBUIDO CADA ITEM DA NOTA A UM ITEM DOS ALUNOS? 
#USA-SE A FUNÇÃO: zip() ex.:
for aluno, nota in zip(alunos, notas):
    print(f'A nota do aluno {aluno.upper()} foi {nota}')


#quando usa a função zip(), ela vai iterar sobre as 2 listas ao mesmo tempo ou mais listas, se as listas forem de tamanhos diferentes, ela vai parar na menor.
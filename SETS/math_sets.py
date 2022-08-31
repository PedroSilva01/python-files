from curses import halfdelay
from turtle import home


homens = {'João', 'Joaquim', 'Alberto', 'Antônio', 'Leonardo', 'Victor', 'Kléber', 'Marcelo', 'Alfredo'}
alta_renda = {'Ana' , 'Joaquim' , 'Joana' , 'Antônio' , 'Kléber' , 'Marcelo' , 'Alfredo' , 'Carla' , 'Adriana'}

print(f'Conjunto de homens: \t{homens}')
print(f'Conjunto de alta renda: \t{alta_renda}\n{"-" * 130}\n')

#Interseção: itens que estão em ambos os conjuntos
homens_alta_renda = homens.intersection(alta_renda)

print(f'Homens com alta renda: {homens_alta_renda}')

#União: A soma de ambos os conjuntos, tirando os que estão repetidos, já que não são suportados
homens_E_alta_renda = homens.union(alta_renda)
print(f'Homens e usúarios de alta renda: {homens_E_alta_renda}')


#Diferença: Itens que estão em apenas um dos conjuntos
homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)
print(f'Usúarios que são homens mas não alta renda: {homens_nao_alta_renda}')
print(f'Usúarios que são alta renda mas não homens: {alta_renda_nao_homens}')

#Diferença Simétrica: Itens que estão em um conjunto ou em outro, mas não em ambos
#em resumo ele vai tirar a intersecção do conjunto
homens_nao_alta_renda_E_mulheres = homens.symmetric_difference(alta_renda)
print(f'Usúarios homens não alta renda e usúarios mulheres alta renda: {homens_nao_alta_renda_E_mulheres}')

#EM TODAS ESSAS FUNÇÕES SE ADICIONAR UM _UPDATE APÓS O COMANDO, AO INVÉS DA VARIAVEL ARMAZENAR O RESULTADO, VAI ACONTECER DE ATUALIZAR O CONJUNTO COM O QUE FOI ESPECIFICADO PELA FUNÇÃO ex.: difference_update()
# AI PODE SE RETIRAR A VARIAEL E DEIXAR APENAS A FUNÇÃO

print(f'Os conjuntos de Homens é um subconjunto de alta renda? {homens.issubset(alta_renda)}') #para saber seum conjunto está contido dentro do outro
print(f'Os conjuntos de Homens é um superconjunto de alta renda? {homens.issuperset(alta_renda)}') #
print(f'Os conjuntos de Homens e alta renda são disjuntos? {homens.isdisjoint(alta_renda)}') #para saber se os dois conjuntos não tem intersecções entre eles.

# PARA FACILITAR AO INVÉS DE CHAMAR A FUNÇÃO É SO FAZER ISSO: 
#   INTERSECÇÃO
print(homens & alta_renda)
#   UNIÃO
print(homens | alta_renda)
#   DIFERENÇA
print(homens - alta_renda)
#   DIFERENÇA SIMÉTRICA
print(homens ^ alta_renda)

#PROX AULA F45 - 4
import  random
CAPACIDADE_MAXIMA_BALDE = 1000

balde = 0

while balde <= CAPACIDADE_MAXIMA_BALDE:
    volume_copo = random.randint(95, 100)

    print(f'O copo foi enxido com {volume_copo}ml')

    balde += volume_copo

    print(f'O volume do balde é de {balde}ml\n')

print('O volume ultrapassou a capacidade máxima')

#O RANDINT NÃO ESTAVA FUNFANDO, ENTÃO EU TIVE QUE IMPORTAR A LIB RANDOM RANDOM.RANDINT(NUMBER_INICIAL, FINAL)

#PROGRAMA DE CONCESSÃO DE APOSENTADORIA
#IREMOS PRECISAR COMO ENTRADAS DE:  IDADE, SEXO, 
# E A SAIDA É A DE CONCESSÃO
idade = int(input('Digite a sua idade: '))
print('Digite \t\n"F" se você do sexo feminino \n\tE \t\n"M" se você for do sexo masculino')
sexo = input('Digite a letra correspondente ao seu sexo: ')
# if (sexo == 'm'):
#     sexo == 'M'
# else:
#     sexo == 'F' 
#AO INVES DE FAZER A ESTRUTURA CONDICIONAL ACIMA, É MAIS SIMPLES COLOCAR ASSIM: IF (sexo.upper() == 'M)
if (sexo.upper() == 'M'): 
    if int(idade) >= 65:
        print('Aposentadoria concedida')

    else:
        print('Aposentadoria negada')

elif (sexo.upper() == 'F'):
    if (idade >= 60):
        print('Aposentadoria concedida')

    else:
        print('Aposentadoria negada')

else:
    print('Insira uma letra valida')
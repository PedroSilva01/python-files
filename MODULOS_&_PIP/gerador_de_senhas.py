import string
import random


tamanho_senha = int(input("Digite quantos digitos voce quer que a sua senha tenha: "))
lista = []
i = 0
for item in range(0, tamanho_senha):
    lista.append(random.choice(string.ascii_letters))

# print(lista)
# print(lista.split("'", ",", "")) ERRADO
print("".join(lista))

'''
    PROX AULA: F
'''

def calcula_media_mediana(notas):
    media = sum(notas)/ len(notas)

    if len(notas) % 2 == 0:
        # Número par de elementos
        indice_ponto_central_menor = int((len(notas)/2) -1)
        indice_ponto_central_maior = int(len(notas)/2)
        ponto_central_menor = notas[indice_ponto_central_menor]
        ponto_central_maior = notas[indice_ponto_central_maior]
        mediana = (ponto_central_maior + ponto_central_menor)/2
    else:
        #Número impar de elementos
        notas_ordenadas = sorted(notas) #o sorted ele torna o item em ordem crescente
        indice_mediana = int(len(notas)/2) #da pra fazer isso pq a contagem começa do 0, então ao dividir por 2 vai somar +1 que corresponde ao indice 0
        mediana = notas_ordenadas[indice_mediana]

    return media, mediana


resul_media, resul_mediana = calcula_media_mediana([4,7,9,5])
print(resul_media, resul_mediana)

#len() calcula o tamanho do item inserido dentro dos ()
#sum() calcula a soma de todos os items inserido dentro dos ()

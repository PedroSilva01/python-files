import json
def monta_computador(cpu, memoria, hd, *precos ,monitor=17, **kwargs):
    print(f'O computador montado foi: \n')
    print(f'\tCPU: {cpu}')
    print(f'\tMEMORIA: {memoria} de RAM')
    print(f'\tHD: {hd} GB')
    print(f'\tPreços praticados')

    for preco in precos:
        print(f'\t\tR$ {preco:.2f}')

    print(f'\tMonitor: {monitor} polegadas') #irá printar tbm quando chamar a função
    print(f'\tOutros atributos: ')

    for chave, valor in kwargs.items():
        print(f'\t\t{chave}: {valor}')
    

# monta_computador(cpu="Core I7", memoria=16,hd=2)
#parametros nomeados, a ordem pode ser qualquer uma,já que está colocando explicitamente os parâmetros.

#PARAMETROS NOMINAIS E VARIAVEIS

#TUDO ALÉM QUE FOR NOMEADO VAI CAIR DENTRO DO **KWARGS

monta_computador("Core I7", 16,2, 5880, 873847, webcam="Webcam Multilaser", teclado="Teclado Multilaser")


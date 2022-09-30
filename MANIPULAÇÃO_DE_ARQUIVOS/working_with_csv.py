'''
    TRABALHANDO COM ARQUIVOS CSV

OBJETIVOS:

1) LER ARQUIVOS DE ENTRADA CSV
2) PROCESSAMENTO (RETIRADA DO CAMPO ID E JUNÇÃO COM NOME E SOBRENOME)
3) GRAVAÇÃO DO ARQUIVO CSV DE SAÍDA

'''

resultado = []
with open("./3.1 - Manipulação de arquivos CSV (Material).csv", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]
    for linha in linhas:
        dados = linha.split(",")
        # print(dados)
        resultado.append(f'{dados[1]} {dados[2]}, {dados[3]}\n')


    pass

with open("./novos_Dados_limpos.csv", "w") as arquivo_saida:
    for pessoa in resultado:
        arquivo_saida.write(pessoa) #para cada pessoa irá escrever a linha no arquivo de saida


# PROX AULA MODULO 14
        
'''
    Como trabalhar com os arquivos?
    TRABALHANDO COM A FUNÇÃO OPEN DA MANIPULAÇÃO DE ARQUIVOS:

       texto    binario
------------------------
L    |  "r"   |   "b"
L/E  |  "r+"  |   "b+"
------------------------
E    |  "w"   |   "wb"
E/L  |  "w+"  |   "wb+"
------------------------
A    |  "a"   |   "ab"
A/L  |  "a+"  |   "ab+"
-------------------------
L = LEITURA (READ)
E = ESCRITA (WRITE)
A = ANEXAR (APPEND)

IREMOS CRIAR UM ARQUIVO DE TEXTO PARA ESSA TABELA
'''

arquivo = open("//home//khazn//Documents//PROGRAMAÇÃO//PYTHON//python//python-files//MANIPULAÇÃO_DE_ARQUIVOS//file_0_0.mp4", 'rb')

arquivo_saida = open("//home//khazn//Documents//PROGRAMAÇÃO//PYTHON//python//python-files//MANIPULAÇÃO_DE_ARQUIVOS//video.mp4", 'wb')


retorno_arquivo = arquivo.read()
arquivo_saida.write(retorno_arquivo) #no arquivo_saida eu to passando os bits do video do arquivo pra ele e criando um nov com esse bits, uma (copy)
#print(retorno_arquivo)

arquivo_saida.close()

arquivo.close()

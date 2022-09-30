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


texto = 'Jornada Python Academy - Manipulação de arquivo'
texto_2 = '\nvenha dominar python'
arquivo = open("//home//khazn//Documents//PROGRAMAÇÃO//PYTHON//python//python-files//MANIPULAÇÃO_DE_ARQUIVOS//dados.txt", 'a')

arquivo.write(texto_2)

# arquivo.write(texto)
# retorno = arquivo.read()
# print(retorno) #vai mostrar o que tem dentro do arquivo
#usa-se o // ao invés de só 1 barra '/' para dizer que está criando um diretório

'''
    Função de fechamento de arquivo, sempre tem que usar!!!
    pois evita que tenha dados corrompidos.
'''

arquivo.close()
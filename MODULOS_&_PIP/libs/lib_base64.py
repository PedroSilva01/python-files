from base64 import b64encode
''' 
    TRANSFORMA BINÁRIOS EM TEXTO
'''

with open("./MODULOS_&_PIP/libs/dados/787504.png", 'rb') as arquivo:
    arquivo_b64 = b64encode(arquivo.read()) #tranformou a imagem para base64

    print(arquivo_b64)
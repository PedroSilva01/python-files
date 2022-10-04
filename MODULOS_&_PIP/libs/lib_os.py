import os
"""
    A lib OS trabalha com os comando internos do pc
"""

# os.mkdir("./MODULOS_&_PIP/libs/arquivos_feitos_com_a_lib_os") #CRIOU UMA PASTA COM ESSE NOME E ENDEREÇO

# for diretorio in os.listdir("./"): #amostra todos os diretorios dentro do diretorio atual
#     print(diretorio)

if os.path.exists("./MODULOS_&_PIP/libs/arquivos_feitos_com_a_lib_os"):
    print("Pasta ja existe, irei apagar ela! \n\t APAGANDO PASTA... \n")
    os.rmdir("./MODULOS_&_PIP/libs/arquivos_feitos_com_a_lib_os")
    print("Pasta excluida com sucesso!!")
else:
    print("Pasta não existente! \n\tcriando ela...")
    os.mkdir("./MODULOS_&_PIP/libs/arquivos_feitos_com_a_lib_os")
    print("Pasta criada com sucesso!!")


print(os.getcwd()) #MOSTRA O DIRETÓRIO ATUAL

# os.rename("./MODULOS_&_PIP/libs/dados/787504.png", "./MODULOS_&_PIP/libs/dados/pretty_image.png")
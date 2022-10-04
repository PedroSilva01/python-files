'''
{
    Módulos são arquivos.py simplesmente isso.
    pacotes sao conjuntos logicos de varios modulos, vulgo uma pasta
    scripts sao os codigos python dentro do modulo.
    todo pacote tem que ter o __init__.py para ser realmente um modulo
    palavras reservadas:    
        IMPORT
        FROM
        AS

}
'''

from operacoes.soma import soma


# soma(10, 20) se nao botar o print ele realiza a operação, mas nao amostra o resultado

print(soma(10, 20))
# import matematica ou import matematica *
"""para nao importar todo o pacote se faz:"""
# from matematica import subtrair #boa pratica
"""ou"""
from matematica import soma as funcao_soma #não muito usual fora de data science
'''melhor:'''
import matematica as mat #abreviou

print(matematica.soma(4, 8))
print(subtrair(8, 4))
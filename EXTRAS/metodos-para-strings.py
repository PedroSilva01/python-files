#metodos para alterar textos
# mensagem = 'i like dogs'
# #para garantir que a primeira letra de cada palavra seja maiuscula ou todas maiusculas ou minusculas
# print(mensagem.capitalize())
# #o .lower() deixa todas minusculas
# #o .capitalize() deixa a primeira letra da frase maiuscula
# # o .upper() deixa todas em maiusculas
# print(mensagem.upper())
# # o .find() permite procurar uma letra ou palavra
# print(mensagem.find("like")) #a resposta que virá é um 2, que significa que ele inicia na posição de index 2
# # o .replace() substitui uma palavra/letra antiga pela a nova ex.:
# print(mensagem.replace('dogs', 'cats')) #substituiu a palavra dog por cats
# # o .strip() remove qualquer espaço que coloque antes da 1 letra da frase
# print(mensagem.center(25))# centraliza a palavra para iniciar na posição 25
# print("men,sa,ge,ch,ei,a,de,v,ir,g,u,las".replace(',', ''))

#ENCADEAMENTO DE FUNÇÕES
arrox = 'njjjsdi4iorfnngjndfkndfjknjnfjrn'
print("      Te;x;;to".strip().replace(';', '').center(25, '*').upper())
print(len(arrox))
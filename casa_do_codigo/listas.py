# Lista também é uma sequência em Python, ou seja, podemos perguntar
# seu tamanho e acessar elementos por índice ou trechos (slices).
# Para saber o tamanho, usamos len(lista). Já para acessar por índice,
# usamos lista[indice] e
# >>> lista = ['impostos', 'salarios', 'altos', 'baixos']
# >>> lista[0]
# 'impostos'
# >>> lista[-1]
# 'baixos'
# >>> lista[2:4]
# ['altos', 'baixos']


# [1,2,3,4]
# [1,"imposto",5]
# [[1, 2, 3],"salario",10]


# EXEMPLO DE LISTA VAZIA E SEU RETORNO COMO FALSE

lista = []
if lista:
    print("Nunca sou executado")
else:
    print("Sempre sou executado")
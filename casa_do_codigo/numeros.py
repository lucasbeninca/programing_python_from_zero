1    #int
1.0  #float
1.   #float
1+2j #complex

#gerando os numeros por meio das funcões embutidas
int(1.0)
int('9')

float('9.2')
float('-inf')
float('+inf')
float('nan')
complex(1, 2)


#exemplo de número complex =====================================================
# 1j é uma sintaxe para criar um número complexo.
# O 'j' aqui é parte da definição do número.
numero_complexo = 1j
print(f"O valor de 1j é {numero_complexo} e o tipo é {type(numero_complexo)}")

# Se você tentar criar uma variável chamada 'j', ela não terá relação
# com a unidade imaginária usada na sintaxe de números complexos.
j = 5
print(f"A variável j agora vale {j} e o tipo é {type(j)}")

# Mesmo com a variável j definida como 5, a sintaxe de número complexo continua funcionando da mesma forma.
outro_complexo = 2 + 3j
print(f"O valor de 2 + 3j ainda é {outro_complexo}")

#== == == == == == == == == == == == == == == == == == == == == == == == == == =
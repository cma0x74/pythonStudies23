# calcula hipotenusa a partir de dois catetos
from math import sqrt
a = eval(input('insere um cateto '))
b = eval(input('insere mais um cateto '))

print(f'a hipotenusa de um triângulo retângulo com catetos {a} e {b} é {sqrt((a ** 2) + (b ** 2)):.2f}')